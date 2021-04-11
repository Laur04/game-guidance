from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect, reverse

from .forms import CreateForm

def index(request):
    return render(request, "games/index.html")

def register(request):
    form = None
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            get_user_model().objects.create_user(username, username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("games:initial"))
    else:
        form = CreateForm()
    return render(request, "games/register.html", context={"form": form})

def initial(request):
    return render(request, "games/initial.html")

def recommendations(request):
    return render(request, "games/recommendations.html")

def browse(request):
    return render(request, "games/browse.html")

def user_games(request):
    return render(request, "games/user-games.html")
