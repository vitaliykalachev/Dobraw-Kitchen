from crypt import methods
import email
from fastapi import FastAPI, APIRouter, Request, Depends, responses, status, Response, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from .. import crud


router = APIRouter(
    prefix='',
    tags=['templates']
)



templates = Jinja2Templates(directory="app/templates")




@router.get("/")
async def index(request: Request, message: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})
   
@router.get("/sweets/bakery/dzen", response_class=HTMLResponse)
async def recipe(request: Request):
    return templates.TemplateResponse("/sweets/bakery/dzen.html", {"request": request})
    



