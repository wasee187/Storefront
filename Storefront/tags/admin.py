from django.contrib import admin
from .models import Tag

# Registering the tags app.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']