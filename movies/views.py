from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(req):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(req, 'movies/index.html', context)

def detail(req, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(req, 'movies/detail.html', context)

@login_required
def like(req, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if req.user in movie.like_users.all():
        movie.like_users.remove(req.user)
    else:
        movie.like_users.add(req.user)
    return redirect('movies:detail', movie_id)

@login_required
def reviews_new(req, movie_id):
    if req.method == 'POST':
        review_form = ReviewForm(req.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = Movie.objects.get(id=movie_id)
            review.user = req.user
            review.save()
    return redirect('movies:detail', movie_id)

@login_required
def reviews_delete(req, movie_id, review_id):
    if req.method == 'POST':
        review = get_object_or_404(Review, id=review_id)
        if review.user == req.user:
            review.delete()
    return redirect('movies:detail', movie_id)

