from fastapi import FastAPI, Depends
from pydantic import BaseModel

class Item(BaseModel):
    name: str | None = "Mmesoma"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/hello")
async def hello(item: Item = Depends(Item)):
    return {"message": f"Heyhey {item.name}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)