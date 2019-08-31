from django.contrib import admin
from .models import PostFile, Comments
from .forms import CommentForm


class CommentsAdminInline(admin.TabularInline):
    model = Comments
    extra = 1
    form = CommentForm


class PostFileAdmin(admin.ModelAdmin):
    model = PostFile
    inlines = [CommentsAdminInline]


admin.site.register(PostFile, PostFileAdmin)

# admin.site.register(Comments)
