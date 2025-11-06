from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a Movie name")
    date = models.DateField(help_text="Enter a Movie date")