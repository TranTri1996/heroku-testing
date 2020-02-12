from __future__ import unicode_literals
from django.db import models


class Accessory(models.Model):
    biker_id = models.IntegerField(default=-1)
    name = models.CharField(max_length=100, null=False, default="")
    description = models.TextField(null=True, default="")
    unit_price = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    market_price = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    like_number = models.IntegerField(null=False, default=0)
    is_active = models.SmallIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "accessory_tab"


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
    email = models.CharField(max_length=100, unique=True)
    hashed_password = models.CharField(max_length=100, null=False, default="")
    password_salt = models.CharField(max_length=128, default="")
    is_active = models.BooleanField(default=1)
    main_address_id = models.IntegerField(null=True, default=-1)
    date_of_birth = models.DateField(null=True)
    gender = models.SmallIntegerField(default=0)
    job = models.CharField(max_length=50, default="")
    facebook = models.CharField(max_length=100, default="")
    like_number = models.IntegerField(null=False, default=0)
    updated_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "biker_tab"


class Token(models.Model):
    token = models.CharField(max_length=255, default="", primary_key=True)
    biker_id = models.IntegerField()
    expiry_time = models.DateTimeField()
    app_type = models.SmallIntegerField(default=1)

    class Meta:
        db_table = 'token_tab'


class Comment(models.Model):
    comment_parent_id = models.IntegerField(default=-1)  # default is have no parent
    biker_id = models.IntegerField(default=-1)
    post_id = models.IntegerField(default=-1)
    accessory_id = models.IntegerField(default=-1)
    content = models.TextField(default="")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment_tab"


class Like(models.Model):
    comment_id = models.IntegerField(default=-1)  # not belong comment
    post_id = models.IntegerField(default=-1)  # not belong post
    biker_id = models.IntegerField(default=-1)  # not belong biker
    accessory_id = models.IntegerField(default=-1)  # not belong accessory
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "like_tab"


class PostImage(models.Model):
    post_id = models.IntegerField(default=-1)
    url = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "post_image_tab"


class Post(models.Model):
    biker_id = models.IntegerField(default=-1)
    like_number = models.IntegerField(null=False, default=0)
    share_number = models.IntegerField(null=False, default=0)
    view_number = models.IntegerField(null=False, default=0)
    title = models.CharField(max_length=255, null=False, default="")
    description = models.TextField(null=True, default="")
    is_active = models.SmallIntegerField(default=1)  # default is active
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "post_tab"
