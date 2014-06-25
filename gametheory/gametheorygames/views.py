from django.shortcuts import render, redirect
from django.http import HttpResponse

from gametheorygames.models import Game

def home_page(request):
	return render(request, 'home.html')
	
def losing_game(request):
	return render(request, 'losing_game.html')
	
def new_losing_game(request):
	game = Game.objects.create()
	return redirect(game)
	
def play_losing_game(request, id):
	return render(request, 'play_losing_game.html')
