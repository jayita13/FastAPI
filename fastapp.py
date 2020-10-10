from typing import List
import spacy
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

nlp = spacy.load("en_core_web_sm")

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    content: str
    comments: List[str] = []


@app.post("/item/")
def post_item(item: Item):
    doc = nlp(item.content)
    ents = []
    for ent in doc.ents:
        ents.append({"text":ent.text,"label":ent.label_})
    return {"message":item.content, "comments":item.comments, "ents":ents}



