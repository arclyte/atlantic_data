from sqlalchemy import Column, Index, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class CustomerModel(DeclarativeBase):
    __tablename__ = 'customer'
    __table_args__ = (
        Index('id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    address = Column(Text)
    state = Column(String(2), nullable=True)
    postal_code = Column(String(5), nullable=True)
