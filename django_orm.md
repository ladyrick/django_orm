# how to convert django to django_orm

1. mv django django_orm
2. replace all `\bdjango\b` to django_orm
3. mv django_orm/template/backends/django.py django_orm/template/backends/django_orm.py
4. add to `django_orm/apps/config.py`

```
class DjangoOrmDefault(AppConfig):
    path = "/"
    name = "django_orm_default"
    label = "django_orm_default"
```

5. modify `django_orm/db/models.py` and add some necessary `import`

```
app_label = "django_orm_default"
app_config = DjangoOrmDefault

# Look for an application configuration to attach the model to.
# app_config = apps.get_containing_app_config(module)
```

6. modify `django_orm/apps/registry.py` and add some necessary `import`

```
apps = Apps(installed_apps=(DjangoOrmDefault("django_orm_default", "django_orm_default"),))
```

7. edit `setup.cfg`. change project name to "**Django_Orm**"
