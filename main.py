import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app= FastAPI()

@app.get("/blog")
def index(limit = 10, published:bool = True, sort:Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {"data": f"{limit} published blogs from the DB"}
    else:
        return {"data": f"{limit} blogs from the DB"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {'data':id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {'data': {'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with {request.title} title"}

# class Kunna (BaseModel):
#     Kunna_length: int
#     Kunna_girth: int
#     Kunna_Kambi: Optional[bool]
#     Kunna_boner: str

# @app.post("/Kunna")
# def Kunna_status(kunner: Kunna):

#     if kunner.Kunna_Kambi:
#         kunner.Kunna_boner = "Standing"
#     else:
#         kunner.Kunna_boner = "sleeping"

#     return {
#             "Client's Kunna length": kunner.Kunna_length,
#             "Client's Kunna girth": kunner.Kunna_girth,
#             "Client's Kunna status": kunner.Kunna_boner
#             }


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=9000)

# pip install -r requirements.txt