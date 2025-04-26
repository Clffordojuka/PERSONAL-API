from sqlalchemy.orm import Session
from personal_api.models import Customer
from personal_api.schemas import CustomerCreate
from fastapi import HTTPException

def create_new_customer(db: Session, customer: CustomerCreate):
    # Check if the email already exists in the database
    db_customer = db.query(Customer).filter(Customer.email == customer.email).first()
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new customer object
    new_customer = Customer(
        customerName=customer.customerName,
        email=customer.email,
        phoneNumber=customer.phoneNumber,
        customerAddress=customer.customerAddress
    )

    # Add the new customer to the database session
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer