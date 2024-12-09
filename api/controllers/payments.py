from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.models import customers as customer_model, payments as payment_model
from api.schemas.customers import CustomerCreate
from api.schemas.payment import PaymentCreate


def create_payment(db: Session, request: PaymentCreate):
    db_customer = db.query(customer_model.Customer).filter(customer_model.Customer.id == request.customer_id).first()
    if not db_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with ID {request.customer_id} not found"
        )

    # Create a new Payment instance
    new_payment = payment_model.Payment(
        card_number=request.card_number,
        exp_month=request.exp_month,
        exp_year=request.exp_year,
        security_code=request.security_code,
        name_on_card=request.name_on_card,
        paying_customer_id=request.paying_customer_id  # Ensure this matches the database schema
    )

    # Add the new Payment to the database session
    db.add(new_payment)
    db.commit()  # Commit the transaction
    db.refresh(new_payment)  # Refresh to get the full object

    return new_payment