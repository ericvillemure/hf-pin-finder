from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/servo/left-click")
def leftClick():
    return {"ok": True, "operation": "left-click"}

@app.put("/servo/right-click")
def rightClick():
    return {"ok": True, "operation": "right-click"}
