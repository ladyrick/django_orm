from django_orm.db import models


class Thing(models.Model):
    num = models.IntegerField()
