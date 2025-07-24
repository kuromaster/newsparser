from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr
    app_name: str
    app_pth: str
    channel_id: int
    pg_user: str
    pg_pwd: SecretStr
    pg_host: str
    pg_dbname: str

    # Начиная со второй версии pydantic, настройки класса настроек задаются
    # через model_config
    # В данном случае будет использоваться файла .env, который будет прочитан
    # с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='config/env', env_file_encoding='utf-8')


config = Settings()

