from django.shortcuts import render, redirect
from django.http import HttpResponse

from gametheorygames.models import GAME_STATES, Game, LosingGame

def home_page(request):
	return render(request, 'home.html')
	
def losing_game(request):
	return render(request, 'losing_game.html')
	
def new_losing_game(request):	
	game = LosingGame.objects.create()
	return redirect(game)
	
def play_losing_game(request, id):
	return render(request, 'play_losing_game.html')
	
def losing_game_Coinbase_callback(request, id):
	game = LosingGame.objects.get(id = id)
	game.state = GAME_STATES["LIVE"]
	game.save()
	return HttpResponse("resolved")
