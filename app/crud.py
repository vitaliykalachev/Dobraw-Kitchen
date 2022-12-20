from sqlalchemy.orm import Session, joinedload

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


def create_recipe(db:Session, recipe: schemas.RecipeCreateIN):
    recipe = models.Recipe(**recipe.dict())
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# def create_user_recipe(db: Session, recipe: schemas.Recipe):
#     db_item = models.Recipe(recipe)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
