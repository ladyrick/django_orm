from django_orm.contrib.admindocs.middleware import XViewMiddleware
from django_orm.http import HttpResponse
from django_orm.utils.decorators import decorator_from_middleware
from django_orm.views.generic import View

xview_dec = decorator_from_middleware(XViewMiddleware)


def xview(request):
    return HttpResponse()


class XViewClass(View):
    def get(self, request):
        return HttpResponse()


class XViewCallableObject(View):
    def __call__(self, request):
        return HttpResponse()
