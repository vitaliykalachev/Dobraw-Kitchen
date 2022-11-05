from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .routers import  template
from pydantic import BaseModel


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(template.router)



@app.get("/")
def main_root():
    return ("Hello Vitaliy")

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


    

