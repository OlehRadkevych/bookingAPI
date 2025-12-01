import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    BASE_URL: str = os.getenv("BASE_URL")
    USERNAME: str = os.getenv("_USER")
    PASSWORD: str = os.getenv("_PASSWORD")
    AUTH_TOKEN: str = os.getenv("AUTH_TOKEN")
