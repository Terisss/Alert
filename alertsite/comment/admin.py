from django.contrib import admin

from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'event', 'author', 'pub_date', 'enable', 'was_published_recently'
    )
    list_filter = ['event', 'pub_date', 'enable']

admin.site.register(Comment, CommentAdmin)
