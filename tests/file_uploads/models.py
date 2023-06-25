from django_orm.db import models


class FileModel(models.Model):
    testfile = models.FileField(upload_to="test_upload")
