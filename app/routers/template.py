from crypt import methods
import email
from fastapi import FastAPI, APIRouter, Request, Depends, responses, status, Response, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from .. import crud


# class Data(BaseModel):
#     firstName: str
#     lastName: str
#     email: str


router = APIRouter(
    prefix='',
    tags=['templates']
)



# class Htmx_template(BaseModel):
#     firstName = str
#     lastName = str
#     email = str

# class Htmx_test(Base):
#     __tablename__ = "htmx_test"
#     id = Column(Integer, primary_key=True, nullable=False)
#     firstName = Column(String, nullable=False)
#     lastName = Column(String, nullable=False)
#     email = Column(String, nullable=False)

templates = Jinja2Templates(directory="app/templates")




@router.get("/")
async def index(request: Request, message: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

# @router.get("/recipe", response_class=HTMLResponse)
# async def recipe(request: Request, id = str):
    
#     return templates.TemplateResponse("recipe.html", {"request": request, "id": id})


   
@router.get("/sweets/bakery/dzen", response_class=HTMLResponse)
async def recipe(request: Request):
    return templates.TemplateResponse("/sweets/bakery/dzen.html", {"request": request})
    

@router.post("/clicked")
async def index(request: Request, message: str = None):
    return {"message": "Clicked"}

@router.get("/test", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@router.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/test_1_edit", response_class=HTMLResponse)
async def contact_edit(request: Request, firstName = "Vitaliy", lastName = "Kala4", email = "email@mail.com"):
    return templates.TemplateResponse("test_1_edit.html", {"request": request, "firstName": firstName, "lastName":lastName, "email": email})
    
@router.get("/test_recipe_edit", response_class=HTMLResponse)
async def contact_edit(request: Request, firstName = "23", lastName = "123"):
    return templates.TemplateResponse("test_recipe_edit.html", {"request": request, "firstName": firstName, "lastName":lastName})
        
    
@router.get("/test_1", response_class=HTMLResponse)
async def contact_edit(request: Request, firstName = "Vitaliy", lastName = "Kala4", email = "email@mail.com"):
    firstName = firstName
    # lastName = "Kala4"
    # email = "kala4@mail.com"
    return templates.TemplateResponse("test_1.html", {"request": request, "firstName": firstName, "lastName":lastName, "email": email})
        
@router.get("/test_2", response_class=HTMLResponse)
async def contact_edit(request: Request, firstName = "123", lastName = "33"):
    
    return templates.TemplateResponse("test_2.html", {"request": request, "firstName": firstName, "lastName":lastName})
        

@router.put("/test_1", response_class=HTMLResponse)
async def contact_edit(request: Request, firstName: str = Form(), lastName: str = Form(), email: str = Form()):
    return templates.TemplateResponse("test_1.html", {"request": request, "firstName": firstName, "lastName":lastName, "email": email})
    
@router.put("/test_2", response_class=HTMLResponse)
async def contact_edit(request: Request, firstName: str = Form(), lastName: str = Form()):
    return templates.TemplateResponse("test_2.html", {"request": request, "firstName": firstName, "lastName":lastName})
    
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














@router.get("/code")
async def other_sweet(request: Request):
    return templates.TemplateResponse("/code.html", {"request": request})

@router.get("/raw/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}



# @router.get("/vegan_raw/example_vegan_raw")
# async def vegan(request: Request):
#     return templates.TemplateResponse("/vegan_raw/example_vegan_raw.html", {"request": request})