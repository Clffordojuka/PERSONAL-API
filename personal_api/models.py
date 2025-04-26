from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from personal_api.database import Base

class Customer(Base):
    __tablename__ = "customer"

    customerID = Column(Integer, primary_key=True, index=True)
    customerName = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    phoneNumber = Column(String(20))
    customerAddress = Column(String(200))
    dateCreated = Column(DateTime(timezone=True), server_default=func.now())