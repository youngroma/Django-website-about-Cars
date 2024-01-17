from django.contrib import admin
from .models import *
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'brand')
    search_fields = ('brand', 'model')
    list_editable = ('is_published', ) #список редактируемых полей
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Car, CarAdmin)
admin.site.register(Category, CategoryAdmin)
