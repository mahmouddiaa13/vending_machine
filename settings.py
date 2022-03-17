import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class PostgresDBSettings(BaseSettings):
    HOST: str = ""
    NAME: str = ""
    USER_NAME: str = ""
    PWD: str = ""

    class Config(BaseSettings.Config):
        env_prefix = "DB_POSTGRES_"


class Security(BaseSettings):
    SECRET_KEY: str = ""
    ALGORITHM: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config(BaseSettings.Config):
        env_prefix = "SECURITY_"


def get_postgres_db_settings():
    return PostgresDBSettings()


def get_security_settings():
    return Security()
