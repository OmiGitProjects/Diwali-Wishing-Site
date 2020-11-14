from django.contrib import admin
from .models import QuotesDatabase

@admin.register(QuotesDatabase)
class QuotesDatabaseAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author', 'timeStamp']