from fastapi import FastAPI
import os
import json

app = FastAPI()
user_db_file = "./user_db.json"

@app.get("/user/{user_Id}")
def get_user(user_Id:int):
    if not user_db_file:
       return []
    
    with open(user_db_file,"r") as file:
     return json.load(file)

@app.post("/user")
def create_user(data:dict):

    with open(user_db_file,"r") as file:
      exsiting_user = json.load(file)
      exsiting_user.append(data)

    with open(user_db_file,"w") as file:
        json.dump(exsiting_user,file,indent=4)
   

@app.put("/user/{user_Id}")
def update_user(user_Id:int, data:dict):
    return {"content":"testing purpose","name":data["name"] ,"age":data["age"]}
    # return {"age":data["age"]}