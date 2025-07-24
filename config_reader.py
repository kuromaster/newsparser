from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr
    # openai_api_key: SecretStr
    app_name: str
    app_pth: str
    channel_id: int
    pg_user: str
    pg_pwd: SecretStr
    pg_host: str
    pg_dbname: str
    # maezztro_tid: int
    # maezztro_name: str
    # maezztro_lastname: str
    # maezztro_phone: str
    # mt_login: str
    # mt_pwd: SecretStr
    # mt_host: str
    # zabbix_login: str
    # zabbix_pwd: str
    # zabbix_http: str
    # group_tid: int
    # mt_backup_pwd: str
    # mt_login_client: str
    # mt_pwd_client: SecretStr
    # taiga_api_user: str
    # taiga_api_user_pwd: SecretStr
    # taiga_url: str
    # jira_api_user: str
    # jira_api_user_pwd: SecretStr
    # jira_url: str
    # wiki_url: str
    # debug: int

    # Начиная со второй версии pydantic, настройки класса настроек задаются
    # через model_config
    # В данном случае будет использоваться файла .env, который будет прочитан
    # с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='config/env', env_file_encoding='utf-8')


# class Variables:
#     # def __init__(self, su_list: List[int]) -> None:
#     #     self.su_list = su_list
#
#     su_list: list
#     test_var: str


# При импорте файла сразу создастся
# и провалидируется объект конфига,
# который можно далее импортировать из разных мест

config = Settings()
# myvars = Variables()
