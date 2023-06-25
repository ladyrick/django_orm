"""
Django's support for templates.

The django_orm.template namespace contains two independent subsystems:

1. Multiple Template Engines: support for pluggable template backends,
   built-in backends and backend-independent APIs
2. Django Template Language: Django's own template engine, including its
   built-in loaders, context processors, tags and filters.

Ideally these subsystems would be implemented in distinct packages. However
keeping them together made the implementation of Multiple Template Engines
less disruptive .

Here's a breakdown of which modules belong to which subsystem.

Multiple Template Engines:

- django_orm.template.backends.*
- django_orm.template.loader
- django_orm.template.response

Django Template Language:

- django_orm.template.base
- django_orm.template.context
- django_orm.template.context_processors
- django_orm.template.loaders.*
- django_orm.template.debug
- django_orm.template.defaultfilters
- django_orm.template.defaulttags
- django_orm.template.engine
- django_orm.template.loader_tags
- django_orm.template.smartif

Shared:

- django_orm.template.utils

"""

# Multiple Template Engines

from .engine import Engine
from .utils import EngineHandler

engines = EngineHandler()

__all__ = ("Engine", "engines")


# Django Template Language

# Public exceptions
from .base import VariableDoesNotExist  # NOQA isort:skip
from .context import Context, ContextPopException, RequestContext  # NOQA isort:skip
from .exceptions import TemplateDoesNotExist, TemplateSyntaxError  # NOQA isort:skip

# Template parts
from .base import (  # NOQA isort:skip
    Node,
    NodeList,
    Origin,
    Template,
    Variable,
)

# Library management
from .library import Library  # NOQA isort:skip

# Import the .autoreload module to trigger the registrations of signals.
from . import autoreload  # NOQA isort:skip


__all__ += ("Template", "Context", "RequestContext")
