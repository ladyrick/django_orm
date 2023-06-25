"""
Invokes django_orm-admin when the django_orm module is run as a script.

Example: python -m django_orm check
"""
from django_orm.core import management

if __name__ == "__main__":
    management.execute_from_command_line()
