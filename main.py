from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Policy(BaseModel):
    policy1: str
    policy2: str 
    policy3: str 
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


@app.get("/")
def index():
    return {"Admin": "Server"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/policy/")
async def get_policy(policy: Policy):
    return { "data" : policy }

@app.post("/policy/")
async def create_policy(policy: Policy):    
    policy.policy1 = "on"
    policy.policy2 = "on"
    policy.policy3 = "off"
    return { "data" : policy }

@app.put("/policy/{item: str}")
async def update_policy(policy: Policy):    
    policy.policy1 = "on"
    return { "data" : policy }

