from sqlalchemy.ext.asyncio import (AsyncSession,
                                    create_async_engine,
                                    async_sessionmaker,
                                    AsyncAttrs)
from sqlalchemy.orm import DeclarativeBase
from src.utils.setting import settings


# //Create Engine wch handles connection

engine = create_async_engine(url = settings.DATABASE_URL, echo = True)

Asynclocalsession = async_sessionmaker(bind=engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass    

async def get_db():
    async with Asynclocalsession() as session:
        yield session