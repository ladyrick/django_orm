from django_orm.http import HttpResponse
from django_orm.utils.decorators import method_decorator
from django_orm.views.decorators.common import no_append_slash
from django_orm.views.generic import View


def empty_view(request, *args, **kwargs):
    return HttpResponse()


@no_append_slash
def sensitive_fbv(request, *args, **kwargs):
    return HttpResponse()


@method_decorator(no_append_slash, name="dispatch")
class SensitiveCBV(View):
    def get(self, *args, **kwargs):
        return HttpResponse()
