import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_email(email: str) -> None:
    if not EMAIL_RE.match(email):
        raise ValueError("Email inválido. Ex: nome@dominio.com")


def validate_name(name: str) -> None:
    if not name or len(name.strip()) < 2:
        raise ValueError("Nome inválido. Use pelo menos 2 caracteres.")


def validate_password(password: str) -> None:
    if len(password) < 8:
        raise ValueError("Senha fraca. Use pelo menos 8 caracteres.")
