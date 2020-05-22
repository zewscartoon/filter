from django.contrib import admin
from .models import Cartoon, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Cartoon)


admin.site.site_title = "Filter Administrator"
admin.site.site_header = "Административная панель FILTER.RU  | 2020 ©"