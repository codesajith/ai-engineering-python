from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class UserRequest(BaseModel):
    name: str
    role: str
    experience: int = Field(ge=0, le=50)

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1)
    temperature: float = Field(ge=0, le=2)

@app.post("/generate")
def generate(request: GenerateRequest):
    return {
        "prompt": request.prompt,
        "temperature": request.temperature,
        "message": "AI request received"
    }

@app.post("/users")
def create_user(user: UserRequest):
    return {
        "message": "User created",
        "user": user
    }

@app.get("/")
def home():
    return {"message": "Hello AI Engineer"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
    "user_id": user_id,
    "message": "User found"
    }

@app.get("/users")
def search_users(role: str):
    return {
        "role": role,
        "message": "Searching users"
    }