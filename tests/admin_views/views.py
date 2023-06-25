from django_orm.contrib.admin.views.decorators import staff_member_required
from django_orm.http import HttpResponse


@staff_member_required
def secure_view(request):
    return HttpResponse(str(request.POST))


@staff_member_required(redirect_field_name="myfield")
def secure_view2(request):
    return HttpResponse(str(request.POST))
