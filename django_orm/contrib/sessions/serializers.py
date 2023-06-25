# RemovedInDjango50Warning.
from django_orm.core.serializers.base import PickleSerializer as BasePickleSerializer
from django_orm.core.signing import JSONSerializer as BaseJSONSerializer

JSONSerializer = BaseJSONSerializer
PickleSerializer = BasePickleSerializer
