from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy


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
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    ingredients = relationship("IngredientPartRecipe", back_populates="recipe")
    recipepart_name = relationship('IngredientPartRecipe', back_populates = 'recipepart')
    
class Ingredient(Base):
    __tablename__ = "ingredients"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    recipesparts = relationship("IngredientPartRecipe",  back_populates="ingredient")
    recipe_ingredient = relationship("IngredientPartRecipe", back_populates="ingredient_recipe")
    
class IngredientPartRecipe(Base):
    __tablename__ = "ingredientspartsrecipes"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    recipepart_id = Column(Integer, ForeignKey("recipesparts.id"), primary_key=True)
    weight = Column(Integer, index=True)
    recipe = relationship("Recipe", back_populates="ingredients")
    recipepart = relationship("Recipe", back_populates = "recipepart_name")
    ingredient = relationship("Ingredient", back_populates="recipesparts")
    ingredient_recipe = relationship("Ingredient", back_populates="recipe_ingredient")
    recipepart_ingredient = relationship('RecipePart', back_populates = 'ingredients')
    recipepart_recipe = relationship('RecipePart', back_populates = 'recipes')
    
    
    ingredient_title = association_proxy(target_collection='ingredient', attr='title')
    recipe_title = association_proxy(target_collection='recipe', attr='title')
    recipepart_name = association_proxy(target_collection='recipepart', attr='name')
    
class RecipePart(Base):
    __tablename__ = "recipesparts"  
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    ingredients = relationship('IngredientPartRecipe', back_populates= 'recipepart_ingredient')
    recipes = relationship("IngredientPartRecipe", back_populates="recipepart_recipe")
    
