from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from IPython import embed
from .models import User
from movies.models import Movie
User =  get_user_model()
# Create your views here.
def signup(req):
    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(req, 'accounts/form.html',context)

def login(req):
    if req.method == "POST":
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            auth_login(req,form.get_user())
        return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(req, 'accounts/form.html',context)

def logout(req):
    auth_logout(req)
    return redirect('movies:index')


def index(req):
    
    accounts  = User.objects.all()
    context = {
        'accounts':accounts
    }
    return render(req, 'accounts/index.html',context)

def detail(req,id):
    User =  get_user_model()
    user = get_object_or_404(User, id=id)
    movies = Movie.objects.filter(like_users=user)
    context ={
        'movies':movies
    }
    return render(req, 'accounts/detail.html',context)