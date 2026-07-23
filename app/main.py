from fastapi import FastAPI
from enum import Enum

class MediaItem(str,Enum):
    id = 1,          # primary key
    title = 
    type:        str          # "movie" | "tv" | "anime" | "game"
    status:      str          # "backlog" | "watching" | "finished" | "dropped"
    rating:      int | None   # 1–10, only once finished
    genres:      str          # e.g. "sci-fi,thriller"
    external_id: str | None   # TMDB / AniList id
    poster_url:  str | None   # pulled from external API
    synopsis:    str | None
    notes:       str | None
    added_at:    datetime
    finished_at: datetime | None


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}

@app.get("/users/me")
async def return_me():
    return {"user": "Bruce Banner"}

@app.get("/users/{user_id}")
async def return_user(user_id:int):
    return {"user":user_id}


@app.get("/users")
async def user_list1():
    return ["Atreades", "Idahao"]

@app.get("/users")
async def user_list1():
    return ["Bill", "Ted"]