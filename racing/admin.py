from __future__ import unicode_literals

from django.contrib import admin

from racing.models.models import Biker, Post

# Register your models here.
admin.site.register(Biker)
admin.site.register(Post)
