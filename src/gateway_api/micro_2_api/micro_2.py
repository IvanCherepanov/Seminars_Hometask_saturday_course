from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json
from random import randint
import os

app = FastAPI()

with open('./micro2.json') as f:
    d = json.load(f)

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/printers")
def read_item(page: int = 0, amount: int = 10):
    new_key = "page"+str(page)
    print(new_key)
    print(len(d))
    return d[new_key][:amount]

@app.get("/main")
def read_temp_data():
    new_key = "page"+str(randint(0, 5))
    keys = ['bar', 'second']
    new_test = d[new_key][randint(0, 5)]
    temp = dict((k, v) for k, v in new_test.items() if k in keys)
    return temp

@app.get("/person")
def read_personal_data():
    new_key = "page"+str(randint(0, 5))
    keys = ['profession', 'company']
    new_test = d[new_key][randint(0, 5)]
    temp = dict((k, v) for k, v in new_test.items() if k in keys)
    return temp

if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))
    uvicorn.run(app, host="0.0.0.0", port=8013)