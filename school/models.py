from django.db import models


class Student(models.Model):
    name = models.TextField(max_length=30, null=True)
    age = models.IntegerField(null=True)

    class Meta:
        ordering = ('id',)

