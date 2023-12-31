from django_orm.contrib.gis.db.backends.base.features import BaseSpatialFeatures
from django_orm.db.backends.postgresql.features import (
    DatabaseFeatures as Psycopg2DatabaseFeatures,
)


class DatabaseFeatures(BaseSpatialFeatures, Psycopg2DatabaseFeatures):
    supports_geography = True
    supports_3d_storage = True
    supports_3d_functions = True
    supports_raster = True
    supports_empty_geometries = True
    empty_intersection_returns_none = False
