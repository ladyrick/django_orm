"""
Test URLs for auth admins.
"""

from django_orm.contrib import admin
from django_orm.contrib.auth.admin import GroupAdmin, UserAdmin
from django_orm.contrib.auth.models import Group, User
from django_orm.contrib.auth.urls import urlpatterns
from django_orm.urls import path

# Create a silo'd admin site for just the user/group admins.
site = admin.AdminSite(name="auth_test_admin")
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)

urlpatterns += [
    path("admin/", site.urls),
]
