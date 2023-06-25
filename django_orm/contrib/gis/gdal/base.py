from django_orm.contrib.gis.gdal.error import GDALException
from django_orm.contrib.gis.ptr import CPointerBase


class GDALBase(CPointerBase):
    null_ptr_exception_class = GDALException
