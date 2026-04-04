import sqlite3
from typing import Optional, List

from user_registry.config import DB_PATH, DATA_DIR, SCHEMA_PATH
from user_registry.domain.models import User
from user_registry.repository.interfaces import IUserRepository


class SQLiteUserRepository(IUserRepository):
    def __init__(self, db_path=DB_PATH):
        DATA_DIR.mkdir(exist_ok=True)
        self.db_path = str(db_path)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        with self._connect() as con:
            schema = SCHEMA_PATH.read_text(encoding="utf-8")
            con.executescript(schema)

    def create(self, user: User) -> None:
        with self._connect() as con:
            con.execute(
                """
                INSERT INTO users (
                    id, name, email, password_hash, password_salt,
                    is_active, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user.id,
                    user.name,
                    user.email,
                    user.password_hash,
                    user.password_salt,
                    int(user.is_active),
                    user.created_at,
                    user.updated_at,
                ),
            )

    def get_by_email(self, email: str) -> Optional[User]:
        with self._connect() as con:
            row = con.execute(
                """
                SELECT id, name, email, password_hash, password_salt, is_active, created_at, updated_at
                FROM users
                WHERE email = ?
                """,
                (email,),
            ).fetchone()

            if not row:
                return None

            return User(
                id=row[0],
                name=row[1],
                email=row[2],
                password_hash=row[3],
                password_salt=row[4],
                is_active=bool(row[5]),
                created_at=row[6],
                updated_at=row[7],
            )

    def list_all(self) -> List[User]:
        with self._connect() as con:
            rows = con.execute(
                """
                SELECT id, name, email, password_hash, password_salt, is_active, created_at, updated_at
                FROM users
                ORDER BY created_at DESC
                """
            ).fetchall()

            return [
                User(
                    id=r[0],
                    name=r[1],
                    email=r[2],
                    password_hash=r[3],
                    password_salt=r[4],
                    is_active=bool(r[5]),
                    created_at=r[6],
                    updated_at=r[7],
                )
                for r in rows
            ]

    def update_name(self, email: str, new_name: str) -> None:
        with self._connect() as con:
            con.execute(
                """
                UPDATE users
                SET name = ?, updated_at = datetime('now')
                WHERE email = ?
                """,
                (new_name, email),
            )

    def set_active(self, email: str, is_active: bool) -> None:
        with self._connect() as con:
            con.execute(
                """
                UPDATE users
                SET is_active = ?, updated_at = datetime('now')
                WHERE email = ?
                """,
                (int(is_active), email),
            )
