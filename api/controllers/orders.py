from httpx import Response
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from api.models import orders as model, customers as customer_model, order_details as detail_model, \
    menu_items as menu_item_model
from api.schemas.orders import OrderCreate


def create(db: Session, request: OrderCreate):
    # Step 1: Create or validate the customer
    new_customer = customer_model.Customer(
        name=request.customer.name,
        email=request.customer.email,
        phone=request.customer.phone,
        address=request.customer.address
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)  # Obtain the new customer ID

    # Step 2: Calculate the total price based on the menu items
    total_price = 0
    order_details = []

    for detail in request.order_details:
        # Fetch the menu item by name
        db_menu_item = db.query(menu_item_model.MenuItem).filter(
            menu_item_model.MenuItem.item_name == detail.menu_item_name
        ).first()
        if not db_menu_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Menu item with name '{detail.menu_item_name}' not found"
            )

        # Calculate price
        item_price = db_menu_item.price * detail.amount
        total_price += item_price

        # Create OrderDetails instance
        order_details.append(detail_model.OrderDetail(
            menu_item_id=db_menu_item.id,
            amount=detail.amount
        ))

    # Step 3: Create the order
    new_order = model.Order(
        date=request.date or datetime.now(),
        status=request.status,
        price=total_price,
        customer_id=new_customer.id
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # Step 4: Add OrderDetails to the database
    for detail in order_details:
        detail.orders = new_order  # Establish the relationship
        db.add(detail)

    try:
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order

def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)