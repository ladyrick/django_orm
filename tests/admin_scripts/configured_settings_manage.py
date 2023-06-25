#!/usr/bin/env python
import sys

from django_orm.conf import settings
from django_orm.core.management import execute_from_command_line

if __name__ == "__main__":
    settings.configure(DEBUG=True, CUSTOM=1)
    execute_from_command_line(sys.argv)
