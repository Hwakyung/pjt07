from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),

    path('<int:movie_id>/reviews/new/', views.reviews_new, name='reviews_new'),
    path('<int:movie_id>/reviews/<int:review_id>/delete/', views.reviews_delete, name='reviews_delete'),

    path('<int:movie_id>/like/', views.like, name='like'), 
]
