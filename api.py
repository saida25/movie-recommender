# filepath: /home/saida/Documents/Projects/movie-recommender/api.py
from fastapi import FastAPI
from ml_recommender import recommend_movies

app = FastAPI()

@app.get("/recommend/{title}")
def recommend(title: str):
    recommendations = recommend_movies(title)
    return {"recommendations": recommendations}