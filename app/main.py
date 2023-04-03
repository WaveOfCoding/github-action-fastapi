import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Status(BaseModel):
    status: str = "ok"


@app.get("/")
async def status():
    return Status()


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
