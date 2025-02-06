import os


class NegativeValueError(ValueError):
    """Custom exception for negative values."""

    def __init__(self, message="Negative values are not allowed"):
        super().__init__(message)


def validate_positive(value):
    """Validate that the value is positive; raise NegativeValueError otherwise."""
    if value < 0:
        raise NegativeValueError(f"Error: {value} is a negative value")
    return value


value = int(input().strip())

if not issubclass(NegativeValueError, ValueError):
    print("NegativeValueError doesn't inherit from built-in ValueError exception\n")

try:
    result = validate_positive(value)
    print(str(result) + "\n")
except NegativeValueError as e:
    print(str(e) + "\n")
