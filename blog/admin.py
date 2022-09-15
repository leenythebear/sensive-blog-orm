from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'published_at')
    raw_id_fields = ['likes', 'tags', 'author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post', 'author', 'published_at')
    raw_id_fields = ['post', 'author']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

