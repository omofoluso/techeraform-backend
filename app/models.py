from django.db import models

class ProgramApplication(models.Model):
    PROGRAM_CHOICES = [
        ('devops', 'DevOps'),
        ('fullstack', 'Fullstack'),
        ('cloud', 'Cloud Computing'),
        # Add more programs as needed
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    SOCIAL_MEDIA_CHOICES = [
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('google', 'Google Search'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    program = models.CharField(max_length=20)
    how_did_you_hear_about_us = models.CharField(max_length=50, blank=True, null=True)
    cover_letter = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.program}"
