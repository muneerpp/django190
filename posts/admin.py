from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["title","timestamp"]
    list_filter = ["updated"]
    search_fields = ["title","content"]


    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
