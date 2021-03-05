from django.shortcuts import render
from django.http import HttpResponse
from . models import Team


# Create your views here.

def index(request):
    team1 = Team()
    team1.name = "Dorcas"
    team1.age = 17
    team1.description = " Im Dorcas and Im 17 years Old"
    team1.offer = False
    team1.image = "team1.jpg"

    team2 = Team()
    team2.name = "John Galekki"
    team2.age = 25
    team2.description = " Im John and Im 20 years Old"
    team2.offer = True
    team2.image = "team2.jpg"
    
    teams = [team1, team2]
    return render(request, "index.html", {"teams":teams})

