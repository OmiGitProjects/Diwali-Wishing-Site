from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, AddWishesForm, CustomPasswordSetForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import QuotesDatabase
from django.contrib.auth.decorators import login_required

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST, label_suffix=' 🧨 ')
            if form.is_valid():
                username = form.cleaned_data.get('username')
                form.save()
                messages.success(request, f'{username}, Your Account is Created!!!')
                return redirect('login')
        else:
            form = UserRegistrationForm(label_suffix=' 🧨 ')

        context = {'form': form}
        return render(request, 'quotesApp/register.html', context)
    else:
        return redirect('homepage')

def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f'{username}, You have Successfully Logged in')
                    return redirect('homepage')
                else:
                    messages.info(request, "Type Correct Username and Password")
                
        else:
            form = UserLoginForm()
        
        context = {'form': form}
        return render(request, 'quotesApp/login_.html', context)
    else:
        return redirect('homepage')

def logout_(request):
    logout(request)
    return redirect('homepage')

@login_required()
def addWishes(request):
    if request.method == 'POST':
        form = AddWishesForm(request.POST)
        if form.is_valid():
            author = request.user.username
            quote = form.cleaned_data.get('quote')

            new_Wish = QuotesDatabase(quote=quote, author=author)
            new_Wish.save()

            messages.success(request, f'{author} Your Wish is Added Successfully!!!')
            return redirect('homepage')
    else:
        form = AddWishesForm()
    context = {'form': form}
    return render(request, 'quotesApp/addWishes.html', context)

@login_required()
def customPasswordChange(request):
    if request.method == 'POST':
        form = CustomPasswordSetForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'{request.user} Your Password Has been Changed Successfully!!!')
            return redirect('homepage')
    else:
        form = CustomPasswordSetForm(user=request.user)
    context = {'form': form}
    return render(request, 'quotesApp/passwordChange.html', context)

@login_required()
def UserProfile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile Info is Updated...')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form': form}
    return render(request, 'quotesApp/profile.html', context)