from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CustomerCreate(BaseModel):
    customerName: str
    email: EmailStr
    phoneNumber: Optional[str] = None
    customerAddress: Optional[str] = None

class CustomerOut(CustomerCreate):
    customerID: int
    dateCreated: datetime

    class Config:
        orm_mode = True