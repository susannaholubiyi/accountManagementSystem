from django.core.exceptions import ValidationError


def validate_pin(pin: str):
    if len(pin) < 4:
        raise ValidationError("Pin must be four digits")
    validate_if_pin_is_numeric(pin)


def validate_if_pin_is_numeric(pin: str):
    if not pin.isdigit():
        raise ValueError("Pin should be all digits")
