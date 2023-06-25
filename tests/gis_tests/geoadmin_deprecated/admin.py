from django_orm.contrib.gis import admin


class UnmodifiableAdmin(admin.OSMGeoAdmin):
    modifiable = False
