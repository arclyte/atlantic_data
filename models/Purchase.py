from sqlalchemy import Column, Index, Integer, Numeric, DateTime
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class PurchaseModel(DeclarativeBase):
    __tablename__ = 'purchase'
    __table_args__ = (
        Index('id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    status = Column(ENUM('new', 'canceled'), nullable=True)
    product_id = Column(Integer, nullable=False)
    amount = Column(Numeric(precision=13, scale=2), nullable=True)
    date = Column(DateTime)
