from sqlalchemy import Column, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class ProductModel(DeclarativeBase):
    __tablename__ = 'product'
    __table_args__ = (
        Index('id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
