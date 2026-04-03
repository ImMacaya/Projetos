from pathlib import Path

DATA_DIR = Path(".data")
DB_PATH = DATA_DIR / "user_registry.db"
SCHEMA_PATH = Path(__file__).parent / "repository" / "schema.sql"