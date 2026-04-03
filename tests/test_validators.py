import pytest
from user_registry.domain.validators import validate_email, validate_name, validate_password

def test_validate_email_ok():
    validate_email("a@b.com")

def test_validate_email_fail():
    with pytest.raises(ValueError):
        validate_email("invalido")

def test_validate_password_fail():
    with pytest.raises(ValueError):
        validate_password("123")