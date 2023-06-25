from django_orm.core import checks
from django_orm.db import models


class ModelRaisingMessages(models.Model):
    @classmethod
    def check(self, **kwargs):
        return [checks.Warning("A warning")]
