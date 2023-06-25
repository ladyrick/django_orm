from django_orm.contrib.gis.geos.error import GEOSException
from django_orm.contrib.gis.ptr import CPointerBase


class GEOSBase(CPointerBase):
    null_ptr_exception_class = GEOSException
