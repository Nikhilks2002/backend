from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)  # transaction ID
    amount = Column(Integer)
    currency = Column(String)
    processed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True), nullable=True)
