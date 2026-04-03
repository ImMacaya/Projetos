from abc import ABC, abstractmethod
from typing import Optional, list
from user_registry.domain.models import User

class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> None: ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional...

    @abstractmethod
    def list_all(self) -> list...

    @abstractmethod
    def update_name(self, email: str, new_name: str) -> None: ...

    @abstractmethod
    def set_active(self, email: str, is_active: bool) -> None: ...