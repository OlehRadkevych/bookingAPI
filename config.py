import os
from dataclasses import dataclass


@dataclass
class Config:
    BASE_URL: str = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
    USERNAME: str = os.getenv("_USER", "admin")
    PASSWORD: str = os.getenv("PASSWORD", "password123")
