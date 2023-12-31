from django.db import models


# Defining the Profile model for storing CV-related information
class Profile(models.Model):
    # Fields to store personal information and CV details
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    work = models.TextField(max_length=2000)
    skills = models.TextField(max_length=20000)

    # Fields for tracking creation and update timestamps
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
