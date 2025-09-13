from fastapi import FastAPI
from pydantic import BaseModel
from .rozgar_bot import spawnAgent   # ab async wala import hoga

app = FastAPI()

class Query(BaseModel):
    text: str

@app.post("/ask")
async def ask_agent(query: Query):
    result = await spawnAgent(query.text)   # ✅ async call
    return {"answer": result}
