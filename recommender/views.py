# filepath: /home/saida/Documents/Projects/movie-recommender/recommender/views.py
import requests
from django.shortcuts import render

def movie_recommendation(request):
    title = request.POST.get("title")
    response = requests.get(f"http://localhost:8001/recommend/{title}")
    try:
        data = response.json()
        movies = data.get("recommendations", [])
    except Exception:
        movies = []
    return render(request, "recommend.html", {"movies": movies})