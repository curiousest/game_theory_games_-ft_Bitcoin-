from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from gametheorygames.models import Game

from gametheorygames.views import home_page, losing_game, play_losing_game

def resolves_to_view(self, url, view):
	found = resolve(url)
	self.assertEqual(found.func, view)
	
def returns_correct_html(self, template, view):
	request = HttpRequest()
	response = view(request)
	expected_html = render_to_string(template)
	self.assertEqual(response.content.decode(), expected_html)

	
class AllPagesTest(TestCase):
	ALL_PAGES_DEF = [
		{'url': '/', 'template': 'home.html', 'view': home_page},
		{'url': '/gametheorygames/losing_game', 'template': 'losing_game.html', 'view': losing_game},
	]
	
	def test_static_pages_resolve(self):
		for page in self.ALL_PAGES_DEF:
			resolves_to_view(self, page['url'], page['view'])
	
	def test_static_pages_return_correct_html(self):
		for page in self.ALL_PAGES_DEF:
			returns_correct_html(self, page['template'], page['view'])
			
	def test_bad_url(self):
		pass
			
class PlayLosingGameTest(TestCase):
	
	def test_uses_losing_game_template(self):
		game = Game.objects.create()
		response = self.client.get('/gametheorygames/play_losing_game/%d/' % (game.id,))
		self.assertTemplateUsed(response, 'play_losing_game.html')
	
	def test_losing_game_resolves_to_view(self):
		game = Game.objects.create()
		found = resolve('/gametheorygames/play_losing_game/%d/' % (game.id,))
		self.assertEqual(found.func, play_losing_game)
		
	def test_create_losing_game_from_POST(self):
		self.client.post('/gametheorygames/losing_game/new')
		
		self.assertEqual(Game.objects.count(), 1)


