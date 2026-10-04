from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_Id}")
def get_user(user_Id:int):
    return f"you are uerid {user_Id}"

@app.post("/user")
def create_user(data:dict):
    return {"content":"testing purpose","name":data["name"] ,"age":data["age"]}
    # return {"age":data["age"]}

@app.put("/user/{user_Id}")
def update_user(user_Id:int, data:dict):
    return {"content":"testing purpose","name":data["name"] ,"age":data["age"]}
    # return {"age":data["age"]}