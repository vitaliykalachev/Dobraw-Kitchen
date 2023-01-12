from fastapi import APIRouter, Depends, Request, HTTPException, status
from app import schemas, crud
from app.models import Item
from fastapi.templating import Jinja2Templates
from app.database import get_db
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime
from .login import oauth2_scheme


router = APIRouter(
    prefix='',
    tags=['Item']
)


templates = Jinja2Templates(directory="app/templates")

@router.post("/items/", response_model=schemas.Item)
def create_item(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    date_posted = datetime.now()
    new_item = crud.create_item(db=db, item=item, date_posted=date_posted, user_id=user_id)
    return new_item



@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/items/{item_id}", response_model=schemas.Item)
def read_one_item(item_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    item = crud.get_item(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item {item_id} does not exist")
    return item




@router.put("/items/{item_id}")
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    existing_item = db.query(Item).filter(Item.id == item_id)
    if not existing_item.first():
        return {"message": f"Item {item_id} doesn't exists "}
    existing_item.update(item.__dict__)
    db.commit()
    return {"message": f"Item {item_id} updated successfully"}

@router.delete("/items/{item_id}")
def delete_item_by_id(item_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    existing_item = db.query(Item).filter(Item.id == item_id)
    if not existing_item.first():
        return {"message": f"Item {item_id} doesn't exists "}
    existing_item.delete()
    db.commit()
    return {"message": f"Item {item_id} deleted successfully" }
