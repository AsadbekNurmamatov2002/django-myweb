from django.contrib import admin
from .models import Post, Categorey, Tag, Message, User

admin.site.register(User)
admin.site.register(Tag)
@admin.register(Categorey)
class Categorey(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
@admin.register(Message)
class PostAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated']
    list_filter = ['body', 'created']
    search_fields = ['body']
    