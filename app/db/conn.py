import asyncio

from sqlalchemy import create_engine, text, insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from config import settings
from db.models.base import Base
from db.models.posts import Posts
from db.models.users import Users


"""
Чистые SQL запросы работают быстрее: SELECT * FROM users.
Составные запросы работают медленнее: ...
"""


# pool_size - Базовое количество подключений к БД
# max_overflow - Дополнительное количество подключений к БД
# Суммарное кол-во подключений = 15. Если больше - sqlalchemy встает на ожидание.
sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)


def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


async def insert_data_users():
    user = Users(email='e2@email.ru', name='Wawa', hashed_password='321')
    async with async_session() as session:
        session.add(user)
        await session.commit()


create_tables()
asyncio.run(insert_data_users())
