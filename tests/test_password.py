from user_registry.security.password import generate_salt, hash_password, verify_password

def test_password_hash_and_verify():
    salt = generate_salt()
    h = hash_password("Senha1234", salt)
    assert verify_password("Senha1234", salt, h) is True
    assert verify_password("Errada", salt, h) is False