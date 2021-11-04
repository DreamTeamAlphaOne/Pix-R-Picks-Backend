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
    score = models.JSONField(default=list, blank=True)
    dateAdded = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])