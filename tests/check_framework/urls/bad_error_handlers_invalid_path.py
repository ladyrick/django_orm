urlpatterns = []

handler400 = "django_orm.views.bad_handler"
handler403 = "django_orm.invalid_module.bad_handler"
handler404 = "invalid_module.bad_handler"
handler500 = "django_orm"
