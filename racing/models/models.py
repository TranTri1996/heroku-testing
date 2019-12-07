from __future__ import unicode_literals
from djongo import models


class Address(models.Model):
    id = models.ObjectIdField(default=1)
    street = models.CharField(max_length=255, null=True, default="")
    sub_district = models.CharField(max_length=25, null=True, default="")
    district = models.CharField(max_length=25, null=True, default="")
    city = models.CharField(max_length=25, null=True, default="")
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)


class Location(models.Model):
    id = models.ObjectIdField(default=1)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)


class Biker(models.Model):
    id = models.ObjectIdField(default=1)
    name = models.CharField(max_length=30, null=False, default="")
    phone = models.CharField(max_length=15, null=False, default="")
    email = models.CharField(max_length=100, null=True)
    addresses = models.ListField(models.EmbeddedModelField(model_container=Address), default=[])
    user_name = models.CharField(max_length=30, null=False, default="")
    hash_password = models.CharField(max_length=100, null=False, default="")
    location = models.EmbeddedModelField(model_container=Location)
    like_number = models.IntegerField(null=False, default=0)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.ObjectIdField(default=1)
    url = models.CharField(max_length=255, null=False)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.url


class Post(models.Model):
    id = models.ObjectIdField(default=1)
    author_id = models.EmbeddedModelField(Biker)
    like_number = models.IntegerField(null=False, default=0)
    share_number = models.IntegerField(null=False, default=0)
    view_number = models.IntegerField(null=False, default=0)
    title = models.CharField(max_length=255, null=False, default="")
    description = models.TextField(null=True, default="")
    images = models.ListField(models.EmbeddedModelField(Image), default=[])
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    id = models.ObjectIdField(default=1)
    post_id = models.EmbeddedModelField(Post)
    author_id = models.EmbeddedModelField(Biker)
    content = models.TextField(default="")
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    id = models.ObjectIdField(default=1)
    comment_id = models.EmbeddedModelField(Comment)
    post_id = models.EmbeddedModelField(Post)
    author_id = models.EmbeddedModelField(Biker)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)


class Accessory(models.Model):
    id = models.ObjectIdField(default=1)
    owner_id = models.EmbeddedModelField(Biker)
    name = models.CharField(max_length=100, null=False, default="")
    description = models.TextField(null=True, default="")
    price = models.DecimalField(null=False, default=0.0, decimal_places=3, max_digits=20)
    like_number = models.IntegerField(null=False, default=0)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
