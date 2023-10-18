from django.contrib import admin
from .models import PostAttachment , Post

# Register your models here.
admin.site.register(Post)
admin.site.register(PostAttachment)