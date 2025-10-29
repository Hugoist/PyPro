from django.core.exceptions import ValidationError


def validate_positive_float(value):
    """Raise ValidationError if value is not positive"""

    if value < 0:
        raise ValidationError('Value must be positive')
