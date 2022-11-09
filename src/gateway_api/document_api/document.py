from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json
import os

app = FastAPI()

with open('../documents.json') as f:
    d = json.load(f)

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/documents/")
def read_item(page: int = 0, amount: int = 10):
    new_key = "page"+str(page)
    print(new_key)
    return d[new_key][:amount]

if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run(app, host="0.0.0.0", port=8010)