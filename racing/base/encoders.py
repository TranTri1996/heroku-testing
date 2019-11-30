import json
import datetime
import decimal
from django.utils import timezone
from django.db import models
from django.core.files import File


class ModelSerializer(object):
    def __call__(self, instance):
        fields = instance._meta.get_concrete_fields_with_model()
        fields = list(f[0].attname for f in fields)
        return dict((f, getattr(instance, f)) for f in fields)


class ExtendedJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            if timezone.is_aware(obj):
                obj = timezone.localtime(obj)
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, datetime.date):
            return str(obj)
        if isinstance(obj, datetime.time):
            return str(obj)
        if isinstance(obj, models.Model):
            return ModelSerializer()(obj)
        if isinstance(obj, File):
            return "File"
        return json.JSONEncoder.default(self, obj)
