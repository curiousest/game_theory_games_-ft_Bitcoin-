from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, 'home.html')
	
def losing_game(request):
	return render(request, 'losing_game.html')
	
def play_losing_game(request, id):
	return render(request, 'play_losing_game.html')
