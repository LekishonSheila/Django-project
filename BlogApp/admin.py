from django.contrib import admin
from .models import Category,Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')  

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'created_at')  
    list_filter = ('category',)


