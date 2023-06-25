try:
    from django_orm.contrib.gis import admin
except ImportError:
    from django_orm.contrib import admin

    admin.GISModelAdmin = admin.ModelAdmin
    # RemovedInDjango50Warning.
    admin.OSMGeoAdmin = admin.ModelAdmin
