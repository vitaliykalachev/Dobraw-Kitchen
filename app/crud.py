from sqlalchemy.orm import Session, joinedload
from .hashing import Hasher
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).options(

        joinedload(models.Recipe.recipepart_ingredient)).where(

            models.Recipe.id == recipe_id).first()


def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).options(joinedload(models.Recipe.recipepart_ingredient)).offset(skip).limit(limit).all()


def create_recipe(db: Session, recipe: schemas.RecipeCreateIN):
    recipe = models.Recipe(**recipe.dict())
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


def create_user(db: Session, user: schemas.UserCreate):
    hash_password = Hasher.get_password_hash(user.password)
    db_user = models.User(
        email=user.email, hashed_password=hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate, date_posted: int, user_id: int):
    db_item = models.Item(**item.dict(),date_posted=date_posted, owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
