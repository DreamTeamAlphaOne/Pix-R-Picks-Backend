from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.urls import reverse

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    dateAdded = models.DateField(auto_now_add=True)
    score = models.CharField(default=0, max_length=10)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])