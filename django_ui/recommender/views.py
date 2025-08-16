import requests
from django.conf import settings
from django.shortcuts import render

FASTAPI_URL = "http://localhost:8000"  # Or your Render URL

def movie_recommendation(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        response = requests.get(f"{FASTAPI_URL}/recommend/{title}")
        return render(request, 'recommendations.html', {
            'movies': response.json()['recommendations']
        })
    return render(request, 'search.html')