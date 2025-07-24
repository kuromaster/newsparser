import asyncpg
from config_reader import config


async def init_db():
    conn = await asyncpg.connect(database=config.pg_dbname,
                                 user=config.pg_user,
                                 password=config.pg_pwd.get_secret_value(),
                                 host=config.pg_host,
                                 # ssl=False,
                                 # host="127.0.0.1",
                                 port=5432)

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS news (
                id SERIAL PRIMARY KEY,
                date_reg TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                title TEXT NULL
            );
    ''')


async def news_is_exist(title: str):
    conn = await asyncpg.connect(database=config.pg_dbname,
                                 user=config.pg_user,
                                 password=config.pg_pwd.get_secret_value(),
                                 host=config.pg_host,
                                 port=5432)
    title_id = await conn.fetchval('SELECT id FROM news WHERE title = $1', title)
    if title_id:
        await conn.close()
        return True
    await conn.close()
    return False


async def pg_execute(query: str):
    conn = await asyncpg.connect(database=config.pg_dbname,
                                 user=config.pg_user,
                                 password=config.pg_pwd.get_secret_value(),
                                 host=config.pg_host,
                                 port=5432)
    async with conn.transaction():
        await conn.execute(query)
    await conn.close()

