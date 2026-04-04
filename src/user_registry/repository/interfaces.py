from abc import ABC, abstractmethod
from typing import Optional, List

from user_registry.domain.models import User


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> None: ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]: ...

    @abstractmethod
    def list_all(self) -> List[User]: ...

    @abstractmethod
    def update_name(self, email: str, new_name: str) -> None: ...

    @abstractmethod
    def set_active(self, email: str, is_active: bool) -> None: ...
