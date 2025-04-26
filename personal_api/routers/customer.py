from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from personal_api.services.customer import create_new_customer  # Import service layer
from personal_api.schemas import CustomerCreate, CustomerOut
from personal_api.database import get_db  # Use the database session dependency

router = APIRouter()

@router.post("/customers", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_new_customer(db, customer)