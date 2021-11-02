from django.contrib import admin
from .models import Movie, CustomUser

# Register your models here.
admin.site.register(Movie)
admin.site.register(CustomUser)