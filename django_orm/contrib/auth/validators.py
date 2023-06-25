import re

from django_orm.core import validators
from django_orm.utils.deconstruct import deconstructible
from django_orm.utils.translation import gettext_lazy as _


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Enter a valid username. This value may contain only English letters, "
        "numbers, and @/./+/-/_ characters."
    )
    flags = re.ASCII


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, and @/./+/-/_ characters."
    )
    flags = 0
