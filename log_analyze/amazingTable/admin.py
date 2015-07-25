from django.contrib import admin

# Register your models here.
from .models import Project, Content, Version, Module

admin.site.register(Project)
admin.site.register(Content)
admin.site.register(Version)
admin.site.register(Module)