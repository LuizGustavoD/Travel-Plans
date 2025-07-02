import os

class Config:
    """Base configuration."""
    API_KEY = os.getenv('API_KEY')