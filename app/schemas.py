from typing import Union, List

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str 
    description: str | None = None
    

class ItemCreate(ItemBase):
    pass 


class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True
        

class UserBase(BaseModel):
    email: str
    
    
class UserCreate(UserBase):
    password: str
    
    
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    
    class Config:
        orm_mode = True


class Ingredient(BaseModel):
    id: int = Field(alias='ingredient_id')
    title: str = Field(alias='ingredient_title')
    weight: int = Field(alias = 'weight')
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class Recipe(BaseModel):
    id: int = Field(alias = 'recipe_id')
    title: str = Field(alias = 'recipe_title')
    description: str | None = None
    
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
 


        
class RecipeSchema(BaseModel):
    ingredients: List[Ingredient]
    
class RecipePartSchema(Recipe):
    recipepart_name: List[RecipeSchema]
    


  
class IngredientSchema(Ingredient):
    recipes: List[Recipe]

