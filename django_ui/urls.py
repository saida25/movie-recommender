
from ml_recommender import views  # Import the views from recommender app
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.movie_recommendation, name='recommend'),
]
