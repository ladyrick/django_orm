from django_orm.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)
