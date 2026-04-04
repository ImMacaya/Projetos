import uuid
from user_registry.domain.models import User
from user_registry.domain.validators import (
    validate_email,
    validate_name,
    validate_password,
)
from user_registry.security.password import (
    generate_salt,
    hash_password,
    verify_password,
)
from user_registry.repository.interfaces import IUserRepository


class UserService:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def create_user(self, name: str, email: str, password: str) -> None:
        validate_name(name)
        validate_email(email)
        validate_password(password)

        if self.repo.get_by_email(email):
            raise ValueError("Já existe um usuário com esse email.")

        salt = generate_salt()
        pwd_hash = hash_password(password, salt)

        now = User.now_iso()
        user = User(
            id=str(uuid.uuid4()),
            name=name.strip(),
            email=email.strip().lower(),
            password_hash=pwd_hash,
            password_salt=salt,
            is_active=True,
            created_at=now,
            updated_at=now,
        )
        self.repo.create(user)

    def login(self, email: str, password: str) -> bool:
        validate_email(email)
        user = self.repo.get_by_email(email.strip().lower())
        if not user:
            return False
        if not user.is_active:
            return False
        return verify_password(password, user.password_salt, user.password_hash)

    def update_name(self, email: str, new_name: str) -> None:
        validate_email(email)
        validate_name(new_name)
        if not self.repo.get_by_email(email):
            raise ValueError("Usuário não encontrado.")
        self.repo.update_name(email, new_name.strip())

    def deactivate(self, email: str) -> None:
        validate_email(email)
        if not self.repo.get_by_email(email):
            raise ValueError("Usuário não encontrado.")
        self.repo.set_active(email, False)

    def activate(self, email: str) -> None:
        validate_email(email)
        if not self.repo.get_by_email(email):
            raise ValueError("Usuário não encontrado.")
        self.repo.set_active(email, True)

    def list_users(self):
        return self.repo.list_all()
