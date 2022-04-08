from ast import Return
from turtle import update
from typing import Optional

from fastapi import FastAPI



app = FastAPI()

class Item(data):
    id: 7
    email:michael.lawson@reqres.in
    first_name:Michael
    last_name:Lawson
    avatar: https://reqres.in/img/faces/7-image.jpg

    id: 8
            email: lindsay.ferguson@reqres.in
            first_name: Lindsay
            last_name: Ferguson
            avatar: https://reqres.in/img/faces/8-image.jpg

    id: 9
            email: tobias.funke@reqres.in
            first_name: Tobias
            last_name: "Funke
            avatar: https://reqres.in/img/faces/9-image.jpg
    
    id: 10
            email: byron.fields@reqres.in
            first_name: Byron
            last_name: Fields
            avatar: https://reqres.in/img/faces/10-image.jpg
    
    id: 11
            email: george.edwards@reqres.in
            first_name: George
            last_name: Edwards
            avatar: https://reqres.in/img/faces/11-image.jpg

    id: 12,
            email: rachel.howell@reqres.in
            first_name: Rachel
            last_name: Howell
            avatar: https://reqres.in/img/faces/12-image.jpg
        

@app.get("/item/{item_id}")
def read_Item(item_id:int item:Item ):
    return {"Item_data":item_data}

@app.put("/item/{item_id}")
def update_item(item_id: int item:Item):
    return {"Item_data":update_Item}

@app.post("/item/{item_id}")
def create_item(item_id:int item:Item):
    return {"Item_data":create_Item}

@app.delete("/item/{item_id}")
def delete_item(item_id:int item:Item):
    return{"Item_data":delete_Item}
