from django.contrib import admin
from .models import MovieSuggestion, MovieSelection

# Register your models here.
admin.site.register(MovieSuggestion)
admin.site.register(MovieSelection)