from ed_domain.core.validation.validation_error import ValidationError


class ValidationResponse:
    def __init__(self, is_valid: bool, errors: list[ValidationError] = []):
        self.is_valid = is_valid
        self.errors = errors

    @staticmethod
    def valid() -> "ValidationResponse":
        return ValidationResponse(is_valid=True)

    @staticmethod
    def invalid(errors: list[ValidationError]) -> "ValidationResponse":
        return ValidationResponse(is_valid=False, errors=errors)
