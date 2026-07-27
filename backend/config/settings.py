"""
=========================================================
Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot
Configuration
Version : 1.0.0
=========================================================
"""

from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:

    PROJECT_NAME = "Pradeep Tamilnadu Travels Bus Ticket Booking Chatbot"

    VERSION = "1.0.0"

    API_PREFIX = "/api/v1"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

    SECRET_KEY = os.getenv("SECRET_KEY", "")

    DATABASE_URL = os.getenv("DATABASE_URL", "")

    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    ALGORITHM = "HS256"


settings = Settings()
