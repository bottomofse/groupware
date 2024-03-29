from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'contents', 'pub_date', 'contributer']

admin.site.register(Post, PostAdmin)
