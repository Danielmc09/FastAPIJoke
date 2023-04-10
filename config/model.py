from sqlalchemy import Column, Integer, String, Date

from config.database import Base, engine


def create_tables():
    Base.metadata.create_all(engine)


class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    joke = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
