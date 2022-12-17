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


class RecipePart(BaseModel):
    recipepart_id: int = Field(alias= 'recipepart_id')
    recipepart_title: str = Field(alias= 'recipepart_title')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        
class Ingredient(RecipePart):
    ingredient_id: int = Field(alias='ingredient_id')
    ingredient_title: str = Field(alias='ingredient_title')
    weight: int = Field(alias = 'weight')
    
    

class Recipe(BaseModel):
    id: int = Field(alias = 'recipe_id')
    title: str = Field(alias = 'recipe_title')
    description: str | None = None
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
 

class RecipeSchema(Recipe):
    recipepart_ingredient: List[Ingredient]   

class RecipeCreate(Recipe):
    recipepart_ingredient: List[Ingredient]          

    
class IngredientSchema(Ingredient):
    recipes: List[Recipe]

