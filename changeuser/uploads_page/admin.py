from django.contrib import admin
from .models import PostFile, Comments


class CommentsAdminInline(admin.TabularInline):
    model = Comments
    max_num = 1


class PostFileAdmin(admin.ModelAdmin):
    model = PostFile

    inlines = [
        CommentsAdminInline
    ]




admin.site.register(PostFile, PostFileAdmin)

# admin.site.register(Comments)