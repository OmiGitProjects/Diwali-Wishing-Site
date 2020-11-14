from django.shortcuts import render
from quotesApp.models import QuotesDatabase

def indexHome(request):
    quotes = QuotesDatabase.objects.all().order_by('-timeStamp')
    context = {'quotes': quotes}
    return render(request, 'wishingApp/index.html', context)