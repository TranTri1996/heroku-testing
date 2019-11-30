from __future__ import unicode_literals

from djongo import models


class Biker(models.Model):
    name = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=True)
    address_id = models.IntegerField(null=False)
    user_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    biker_id = models.CharField(max_length=24, null=False)
    status = models.TextField(null=True)

    def __str__(self):
        return self.status
