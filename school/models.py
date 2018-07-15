from django.db import models
import datetime
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache


def change_api_updated_at(sender=None, instance=None, *args, **kwargs):
    cache.set('api_updated_at_timestamp', datetime.datetime.utcnow())


class Student(models.Model):
    name = models.TextField(max_length=30, null=True)
    age = models.IntegerField(null=True)

    class Meta:
        ordering = ('id',)


for model in [Student]:
    post_save.connect(receiver=change_api_updated_at, sender=model)
    post_delete.connect(receiver=change_api_updated_at, sender=model)
