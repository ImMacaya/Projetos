import os
import hashlib
import hmac
import base64

_ITERATIONS = 120_000
_ALG = "sha256"
_SALT_BYTES = 16
_KEY_BYTES = 32


def generate_salt() -> str:
    return base64.b64encode(os.urandom(_SALT_BYTES)).decode("utf-8")


def hash_password(password: str, salt_b64: str) -> str:
    salt = base64.b64decode(salt_b64.encode("utf-8"))
    key = hashlib.pbkdf2_hmac(
        _ALG, password.encode("utf-8"), salt, _ITERATIONS, dklen=_KEY_BYTES
    )
    return base64.b64encode(key).decode("utf-8")


def verify_password(password: str, salt_b64: str, expected_hash_b64: str) -> bool:
    computed = hash_password(password, salt_b64)
    return hmac.compare_digest(computed, expected_hash_b64)
