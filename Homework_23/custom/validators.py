import re

from django.core.exceptions import ValidationError


def validate_hex(value):
    if not re.match(r'^#([A-Fa-f0-9]{6})$', value):
        raise ValidationError('Enter correct hex value')
