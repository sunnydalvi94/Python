from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Address:
    city:str
    state:str


class User(BaseModel):
    name:str
    address:Address

@app.post("/user")
def create_user(user:User):
   return user


## so when user send number or different than above format it will shows error.