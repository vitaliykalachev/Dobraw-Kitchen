from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app import schemas, crud
from sqlalchemy.orm import Session
from app.database import  get_db
from typing import List


router = APIRouter(
    prefix='',
    tags=['Recipe']
)


templates = Jinja2Templates(directory="app/templates")

@router.post("/recipes/", response_model=schemas.RecipeCreateOUT)
def create_recipe(
    recipe: schemas.RecipeCreateIN, db: Session = Depends(get_db)
):
    return crud.create_recipe(db=db, recipe=recipe)


@router.get("/recipes/",
         response_model=List[schemas.RecipeSchema],
         response_model_by_alias=False)
async def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes =  crud.get_recipes(db, skip=skip, limit=limit)

    return recipes


@router.get("/recipes/{recipe_id}",
         response_class=HTMLResponse,
         response_model=schemas.RecipeSchema,
         response_model_by_alias=False)
async def get_recipe(request: Request, recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    context = {"request": request, "recipe": recipe}
    return templates.TemplateResponse("recipe.html", context)
