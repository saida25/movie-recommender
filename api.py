from fastapi import FastAPI
from ml_recommender import recommend_movies

app = FastAPI()

@app.get("/recommend/{title}")
async def recommend(title: str):
    return {"recommendations": recommend_movies(title).tolist()}