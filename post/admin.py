from django.contrib import admin
from.models import BlogPost
from.models import Comment
from.models import Category
from.models import Tag
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "content", "created_at", "categories", "tags")
admin.site.register(BlogPost, BlogPostAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "blog_post", "content", "created_at")
admin.site.register(Comment, CommentAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name")
admin.site.register = (Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name")
admin.site.register = (Tag, TagAdmin)