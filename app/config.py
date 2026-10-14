
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = Path(
    os.getenv(
        "DATABASE_PATH",
        str(BASE_DIR / "students.db"),
    )
)

APP_NAME = "StudentHub API"
APP_VERSION = "1.0.0"
