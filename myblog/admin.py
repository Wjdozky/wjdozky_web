from django.contrib import admin
from .models import blog_post,home,about_me
admin.site.register(blog_post)
admin.site.register(home)
admin.site.register(about_me)
