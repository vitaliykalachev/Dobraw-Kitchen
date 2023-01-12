from typing import Union, List
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Request, Form, Response, responses, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from app.routers import template, item, user, recipe
from app.models import User
from app import crud, models, schemas
from app.database import Sessionlocal, engine, get_db
from crypt import methods
from app.hashing import Hasher
from jose import jwt
from app.config import settings

models.Base.metadata.create_all(bind=engine)

# from sqlalchemy.schema import DropTable
# from sqlalchemy.ext.compiler import compiles


app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(user.router)
app.include_router(recipe.router)
app.include_router(item.router)
app.include_router(template.router)


templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def main_root():
    return ("Hello Vitaliy")


@app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors = []

    if len(password) < 6:
        errors.append("Password should be > 6 character")
        return templates.TemplateResponse("register.html", {"request": request, "errors": errors})
    new_user = User(
        email=email, hashed_password=Hasher.get_password_hash(password))

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return responses.RedirectResponse("/?message=Succesfully Registered", status_code=status.HTTP_302_FOUND)
    except IntegrityError:
        errors.append("Email already exists")
        return templates.TemplateResponse("register.html", {"request": request, "errors": errors})


@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(response: Response, request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors = []
    if not email:
        errors.append("Please Enter valid Email")
    if not password:
        errors.append("Password enter password")
    if len(errors) > 0:
        return templates.TemplateResponse(
            "login.html", {"request": request, "errors": errors}
        )
    try:
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            errors.append("Email does not exists")
            return templates.TemplateResponse(
                "login.html", {"request": request, "errors": errors}
            )
        else:
            if Hasher.verify_password(password, user.password):
                data = {"sub": email}
                jwt_token = jwt.encode(
                    data, settings.secret_key, algorithm=settings.algorithm
                )
                # if we redirect response in below way, it will not set the cookie
                # return responses.RedirectResponse("/?msg=Login Successfull", status_code=status.HTTP_302_FOUND)
                msg = "Login Successful"
                response = templates.TemplateResponse(
                    "login.html", {"request": request, "msg": msg}
                )
                response.set_cookie(
                    key="access_token", value=f"Bearer {jwt_token}", httponly=True
                )
                return response
            else:
                errors.append("Invalid Password")
                return templates.TemplateResponse(
                    "login.html", {"request": request, "errors": errors}
                )
    except:
        errors.append(
            "Something Wrong while authentication or storing tokens!")
        return templates.TemplateResponse(
            "login.html", {"request": request, "errors": errors}
        )

# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)
