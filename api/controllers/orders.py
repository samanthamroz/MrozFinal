from datetime import datetime

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model, customers as customer_model, order_details as detail_model, menu_items as menu_item_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    # Validate customer existence
    db_customer = db.query(customer_model.Customer).filter(customer_model.Customer.id == request.customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

    # Create the Order instance
    new_order = model.Order(
        date=request.date or datetime.now(),
        status=request.status,
        price=request.price,
        customer_id=request.customer_id
    )

    try:
        # Add OrderDetails
        for detail in request.order_details:
            # Validate menu_item existence
            db_menu_item = db.query(menu_item_model.MenuItem).filter(
                menu_item_model.MenuItem.id == detail.menu_item_id).first()
            if not db_menu_item:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Menu item with id {detail.menu_item_id} not found")

            new_detail = detail_model.OrderDetail(
                menu_item_id=request.menu_item_id,  # Setting relationship
                amount=detail.amount
            )
            db.add(new_detail)

        db.add(new_order)
        db.commit()
        db.refresh(new_order)
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
