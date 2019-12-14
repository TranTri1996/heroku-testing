from __future__ import unicode_literals
from django.db import models


class BikerAddress(models.Model):
    address = models.CharField(max_length=255, default="")
    contact_name = models.CharField(max_length=255, default="")
    contact_phone = models.CharField(max_length=15, default="")
    biker_id = models.BigIntegerField(db_index=True)
    district_id = models.BigIntegerField()
    province_id = models.BigIntegerField()
    ward_id = models.BigIntegerField()
    longitude = models.DecimalField(decimal_places=6, max_digits=20, default=0)
    latitude = models.DecimalField(decimal_places=6, max_digits=20, default=0)
    type = models.SmallIntegerField(default=0)
    deleted = models.SmallIntegerField(default=0)
    updated_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "biker_address_tab"


class Biker(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    user_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=100)
    hash_password = models.CharField(max_length=100, null=False, default="")
    password_salt = models.CharField(max_length=128)
    is_active = models.BooleanField(default=1)
    main_address_id = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.SmallIntegerField(default=0)
    job = models.CharField(max_length=50, default="")
    facebook = models.CharField(max_length=100, default="")
    like_number = models.IntegerField(null=False, default=0)
    updated_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "biker_tab"


class PostImage(models.Model):
    post_id = models.IntegerField()
    url = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "post_image_tab"


class Post(models.Model):
    author_id = models.ForeignKey(Biker, on_delete=models.CASCADE, default="", blank=True)
    like_number = models.IntegerField(null=False, default=0)
    share_number = models.IntegerField(null=False, default=0)
    view_number = models.IntegerField(null=False, default=0)
    title = models.CharField(max_length=255, null=False, default="")
    description = models.TextField(null=True, default="")
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "post_tab"


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default="", blank=True)
    author_id = models.ForeignKey(Biker, on_delete=models.CASCADE, default="", blank=True)
    content = models.TextField(default="")
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "comment_tab"

    def __str__(self):
        return self.content


class Like(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, default="", blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default="", blank=True)
    author_id = models.ForeignKey(Biker, on_delete=models.CASCADE, default="", blank=True)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "like_tab"


class Accessory(models.Model):
    owner_id = models.ForeignKey(Biker, on_delete=models.CASCADE, default="", blank=True)
    name = models.CharField(max_length=100, null=False, default="")
    description = models.TextField(null=True, default="")
    price = models.DecimalField(null=False, default=0.0, decimal_places=3, max_digits=20)
    like_number = models.IntegerField(null=False, default=0)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "accessory_tab"
