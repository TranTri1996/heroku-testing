from __future__ import unicode_literals

from django.contrib import admin

from .models import Biker, Post

# Register your models here.
admin.site.register(Biker)
admin.site.register(Post)
