from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date_posted = Column(DateTime, default= func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # ingredients_recipe = relationship("IngredientPartRecipe", back_populates="ingredients")
    recipepart_ingredient = relationship('IngredientPartRecipe', back_populates = 'recipe')
    
class Ingredient(Base):
    __tablename__ = "ingredients"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, index=True)
    # recipe_part = relationship("RecipePart",  back_populates="ingredient")
    recipe_ingredient = relationship("IngredientPartRecipe",  back_populates="ingredient")
    
class IngredientPartRecipe(Base):
    __tablename__ = "ingredientspartsrecipes"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    recipepart_id = Column(Integer, ForeignKey("recipesparts.id"))
    weight = Column(Integer, index=True)
    recipe = relationship("Recipe", back_populates="recipepart_ingredient")
    recipepart = relationship("RecipePart", back_populates = "recipe")
    ingredients = relationship("RecipePart", back_populates="ingredients_recipe")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredient")
    # recipepart_ingredient = relationship('RecipePart', back_populates = 'ingredients')
    # recipepart_recipe = relationship('RecipePart', back_populates = 'recipes')
    
    
    ingredient_title = association_proxy(target_collection='ingredient', attr='title')
    recipe_title = association_proxy(target_collection='recipe', attr='title')

    recipepart_title = association_proxy(target_collection='recipepart', attr='title')
    # recipe_description = association_proxy(target_collection='recipe', attr='description')

class RecipePart(Base):
    __tablename__ = 'recipesparts'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    # ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    # ingredientpartrecipe_id = Column(Integer, ForeignKey("ingredientspartsrecipes.id"), primary_key=True)
    
    title = Column(String, index=True)
    # weight = Column(Integer, index=True)
    ingredients_recipe = relationship("IngredientPartRecipe", back_populates="ingredients")
    # ingredient = relationship("Ingredient", back_populates="recipe_ingredient")
    # ingredients = relationship('IngredientPartRecipe', back_populates= 'recipepart_ingredient')
    recipe = relationship("IngredientPartRecipe", back_populates="recipepart")
    
    # ingredient_title = association_proxy(target_collection='ingredient', attr='title')