from httpx import Response
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from api.models import menu_items as model
from api.schemas.menu_items import MenuItemCreate


def create(db: Session, request: MenuItemCreate):
    try:
        # Create a new MenuItem instance
        new_menu_item = model.MenuItem(
            item_name=request.item_name,
            price=request.price,
            category=request.category
        )

        # Add the new MenuItem to the database session
        db.add(new_menu_item)
        db.commit()  # Commit the transaction
        db.refresh(new_menu_item)  # Refresh to get the full object

        return new_menu_item
    except Exception as e:
        db.rollback()  # Roll back in case of error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)  # Provide an error message
        )

def read_all(db: Session):
    try:
        result = db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
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
        item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)