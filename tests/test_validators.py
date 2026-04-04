import pytest
from user_registry.domain.validators import (
    validate_email,
    validate_name,
    validate_password,
)


def test_validate_email_ok():
    validate_email("a@b.com")


def test_validate_email_fail():
    with pytest.raises(ValueError):
        validate_email("invalido")


def test_validate_password_fail():
    with pytest.raises(ValueError):
        validate_password("123")


def test_validate_name_ok():
    validate_name("Daniel")


def test_validate_name_fail_empty():
    with pytest.raises(ValueError):
        validate_name("")


def test_validate_name_fail_too_short():
    with pytest.raises(ValueError):
        validate_name("A")
