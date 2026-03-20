from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "DevOps Task Manager"
    app_version: str = "1.0.0"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()