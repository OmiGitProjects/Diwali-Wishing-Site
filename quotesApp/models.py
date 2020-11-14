from django.db import models

class QuotesDatabase(models.Model):
    quote = models.CharField(max_length=1000, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)