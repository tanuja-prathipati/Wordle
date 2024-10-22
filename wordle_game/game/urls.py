from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page of the game.
    path('play/', views.play, name='play'),  # Handles game logic on form submission.
]
