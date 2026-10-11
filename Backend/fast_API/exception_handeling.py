from fastapi import FastAPI,HTTPException
import os
import json

app = FastAPI()
user_db_file = "./user_db.json"

@app.get("/user/{user_Id}")
def get_user(user_Id:int):
    if user_Id!=5 :
       raise HTTPException(status_code=404, detail="user not found: ( this error comes form httpexception)")
    if not user_db_file:
       return []
    
    with open(user_db_file,"r") as file:
     return json.load(file)

