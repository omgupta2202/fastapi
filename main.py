
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from pymongo import MongoClient

conn = MongoClient("mongodb+srv://omgupta2202:Jhy9EXpA4Zl57yuk@mongolearn.6ajoyeg.mongodb.net/")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "notes": doc["notes"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})
