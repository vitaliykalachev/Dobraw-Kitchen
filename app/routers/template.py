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
    

@router.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

    

# @router.post("/register")
# async def register(request: Request, db: Session = Depends(get_db)):
#     form = await request.form()
#     email = form.get("email")
#     password = form.get("password")
#     errors = []
    
#     if len(password) < 6:
#         errors.append("Password should be > 6 character")
#         return templates.TemplateResponse("register.html", {"request": request, "errors": errors})
#     new_user = User(email=email, password=utils.hash(password))
    
#     try: 
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return responses.RedirectResponse("/?message=Succesfully Registered", status_code=status.HTTP_302_FOUND)
#     except IntegrityError:
#         errors.append("Email already exists")
#         return templates.TemplateResponse("register.html", {"request": request, "errors": errors})
    
# @router.get("/login")
# async def user_login(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})


