from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel
from .routers import template
from pydantic import BaseModel
from . import crud, models, schemas
from .database import Sessionlocal, engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(template.router)


@app.get("/")
def main_root():
    return ("Hello Vitaliy")


# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/recipes/", response_model=schemas.RecipeSchema)
def read_recipe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes


@app.get("/recipes/{recipe_id}", response_model=schemas.RecipeSchema,
         response_model_exclude={'description'}, response_model_by_alias=False)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# @app.get("/books/{id}", response_model=BookSchema,
#          response_model_exclude={'blurb'}, response_model_by_alias=False)
# async def get_book(id: int, db: Session = Depends(get_db)):
#     db_book = db.query(Book).options(joinedload(Book.authors)).\
#         where(Book.id == id).one()
#     return db_book


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
