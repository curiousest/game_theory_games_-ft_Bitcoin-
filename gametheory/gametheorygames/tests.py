from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from gametheorygames.views import home_page, losing_game

class HomePageTest(TestCase):
	
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class NewGameTest(TestCase):
	
	def test_game_pages_resolve(self):
		found = resolve('/gametheorygames/losing_game')
		self.assertEqual(found.func, losing_game)

	def test_game_page_returns_correct_html(self):
		request = HttpRequest()
		response = losing_game(request)
		expected_html = render_to_string('losing_game.html')
		self.assertEqual(response.content.decode(), expected_html)
