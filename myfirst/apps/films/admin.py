from django.contrib import admin
from .models import Film, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Film)
