from sys import stderr
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from gametheorygames.models import GAME_STATES, Game, LosingGame

from gametheorygames.views import home_page, losing_game, play_losing_game, losing_game_Coinbase_callback

from hashlib import sha256
 
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
 
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')
 
def is_valid_bitcoin_address(address):
    bcbytes = decode_base58(address, 25)
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]

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
		game = LosingGame.objects.create()
		response = self.client.get('/gametheorygames/losing_game/%d/' % (game.id,))
		self.assertTemplateUsed(response, 'play_losing_game.html')
	
	def test_losing_game_resolves_to_view(self):
		game = LosingGame.objects.create()
		found = resolve('/gametheorygames/losing_game/%d/' % (game.id,))
		self.assertEqual(found.func, play_losing_game)
		
	def test_create_losing_game_from_POST(self):
		self.client.post('/gametheorygames/losing_game/new')
		
		self.assertEqual(LosingGame.objects.count(), 1)
		self.assertEqual(Game.objects.count(), 1)
		
	def test_game_initial_state_correct(self):
		game = LosingGame.objects.create()
		
		self.assertEqual(game.state, GAME_STATES["CREATED"])
		
	def test_losing_game_coinbase_callback_url_resolves(self):
		game = LosingGame.objects.create()
		found = resolve('/gametheorygames/losing_game/%d/coinbase_callback/' % (game.id,))
		self.assertEqual(found.func, losing_game_Coinbase_callback)
		
	def test_coinbase_create_iframe_callback_url_changes_game_state(self):
		
		game = LosingGame.objects.create()

		self.client.post(
			'/gametheorygames/losing_game/' + game.get_Coinbase_callback_url(),
			data={
			  "success": True,
			  "button": {
				"code": "93865b9cae83706ae59220c013bc0afd",
				"type": "buy_now",
				"style": "custom_large",
				"text": "Pay With Bitcoin",
				"name": "test",
				"description": "Sample description",
				"custom": "Order123",
				"callback_url": "/gametheorygames/losing_game/%d/coinbase_callback/" % (game.id,),
				"price": {
				  "cents": 123,
				  "currency_iso": "USD"
				}
			  }
			}
		)
		
		game = LosingGame.objects.get(id = game.id)
		
		self.assertEqual(game.state, GAME_STATES["LIVE"])
		
	def test_bad_code_coinbase_create_iframe_callback_url_doesnt_change_game_state(self):
		game = LosingGame.objects.create()

		self.client.post(
			'/gametheorygames/losing_game/' + game.get_Coinbase_callback_url(),
			data={
			  "success": True,
			  "button": {
				"code": "random9cae83706ae59220c013bc0afd",
				"type": "buy_now",
				"style": "custom_large",
				"text": "Pay With Bitcoin",
				"name": "test",
				"description": "Sample description",
				"custom": "Order123",
				"callback_url": "/gametheorygames/losing_game/" + game.get_Coinbase_callback_url(),
				"price": {
				  "cents": 123,
				  "currency_iso": "USD"
				}
			  }
			}
		)
		
		game = LosingGame.objects.get(id = game.id)
		
		self.assertEqual(game.state, GAME_STATES["CREATED"])
		
	def test_create_losing_game_gets_valid_bitcoin_address(self):
		self.client.post('/gametheorygames/losing_game/new')
		
		game = LosingGame.objects.first()
		
		self.assertTrue(is_valid_bitcoin_address(game.depositAddress))	
		
	def test_create_losing_game_has_unique_order_number(self):
		pass
	
	def test_coinbase_iframe_callback_is_validated(self):
		pass
	
	def test_coinbase_iframe_callback_only_works_once(self):
		pass
	
	def test_page_checks_game_state_change(self):
		pass
	
	def test_game_completed_uses_game_completed_template(self):
		pass
