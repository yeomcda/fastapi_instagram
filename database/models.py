from config.database import Base
from sqlalchemy import Column, Integer, String


class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)
    password = Column(String(256), nullable=False)
