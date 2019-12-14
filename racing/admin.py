from __future__ import unicode_literals

from django.contrib import admin

from racing.models.models import Biker, Post, Comment, Like, Accessory

# Register your models here.

admin.register(Biker)
admin.register(Post)
admin.register(Comment)
admin.register(Like)
admin.register(Accessory)
