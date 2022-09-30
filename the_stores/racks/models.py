from django.db import models

class django_rack(models.Model):
    subject=models.CharField(max_length=250)
    explanation= models.CharField(max_length=10000)
    tips_and_tricks=models.CharField(max_length=250)
    code = models.TextField(null=True)
    
class python_rack(models.Model):
    subject=models.CharField(max_length=250)
    explanation= models.CharField(max_length=10000)
    tips_and_tricks=models.CharField(max_length=250)
    code = models.TextField(null=True)
