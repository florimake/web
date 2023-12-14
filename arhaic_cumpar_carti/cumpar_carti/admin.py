from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(HeaderParagraf)
class HeaderParagrafAdmin(admin.ModelAdmin):
    list_display = ("titlu", "paragraf1", "paragraf2")
    prepopulated_fields = {"slug": ("titlu",)}
    
@admin.register(Paragraf)
class ParagrafAdmin(admin.ModelAdmin):
    list_display = ("titlu", "paragraf")
    prepopulated_fields = {"slug": ("paragraf",)}
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("nume", "tel", "email")
    prepopulated_fields = {"slug": ("nume", "tel")}