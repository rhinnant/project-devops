# models.py in your 'accounts' app
from django.contrib.auth.models import User
from django.db import models

class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Administrator'),
        ('support', 'Support Staff'),
        ('user', 'Regular User'),
    ], default='user')

    def __str__(self):
        return f"{self.user.username}'s profile"
