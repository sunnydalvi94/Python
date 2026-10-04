from fastapi import FastAPI

app = FastAPI()

@app.get("/users")

def get_users():
      return [{'name':'rahul','age':24},{'name':'gita','age':22}]

