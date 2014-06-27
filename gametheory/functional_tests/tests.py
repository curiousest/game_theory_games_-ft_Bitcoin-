from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
	
	def test_play_losing_game(self):
		
		# Ida visits homepage
		self.browser.get(self.live_server_url)
		
		# Ida looks at page title and heading
		self.assertIn('Game Theory', self.browser.title)
		
		# She sees that she can play the losing game, among others
		table = self.browser.find_element_by_id('id_game_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('The Losing Game', ['The Losing Game' for row in rows])

		# She chooses to play the losing game
		losing_game_button = table.find_element_by_id('id_losing_game_button')
		self.browser.get(losing_game_button.get_attribute('href'))
		self.assertIn('The Losing Game', self.browser.title)
		
		# The losing game is described to her
		game_description = self.browser.find_element_by_id('id_game_description')
		self.assertIn('Losing Game', game_description.text)
		
		# She chooses to start playing the game
		play_game_button = self.browser.find_element_by_id('id_play_game_button')
		play_game_button.click()
		
		# She is taken to the game page and sees that she has a special url for her game
		self.assertIn('Playing The Losing Game', self.browser.title)
		ida_game_url = self.browser.current_url
		self.assertRegex(ida_game_url, '/losing_game/.+')
		
		# She sees an address to send BTC to and the amount that she has to send to that address
		coinbase_iframe = self.browser.find_element_by_css_selector('iframe')
		self.assertEqual(coinbase_iframe.get_attribute('src'), 'https://coinbase.com/inline_payments/4d4b84bbad4508b64b61d372ea394dad')
		
		# She sends BTC to that address
		# The game recognizes that she has sent the money and updates Ida's game page
		# She is told that she lost and is thanked for playing
		wait = WebDriverWait(self.browser, 20)
			
		win_lose_message = self.browser.find_element_by_id('id_win_lose_message')
		self.assertIn('game finished', win_lose_message.text)
		self.assertIn('you lose', win_lose_message.text)
		
		# She leaves for a second, then returns to her special URL to look at her result again. 
		self.browser.get('http://www.bing.com')
		self.browser.get(ida_game_url)
		
		win_lose_message = self.browser.find_element_by_id('id_win_lose_message')
		self.assertIn('game finished', win_lose_message.text)
		self.assertIn('you lose', win_lose_message.text)
		
	def test_three_people_play_losing_game(self):
		pass
		# Ida chooses to play the losing game
		# She sees the play game page
		
		# Peter chooses to play the losing game
		# He sees the play game page
		# His game page url is different
		# Peter sends BTC
		# The game recognizes that he has sent the money and updates Peter's game page
		# He is told that she lost and is thanked for playing
		
		# Ida's game page remains unchanged
		
		# Norma chooses to play the losing game
		# She sees the play game page
		
		# Ida sends BTC
		# The game recognizes that she has sent the money and updates Ida's game page
		# She is told that she lost and is thanked for playing
		
		# Norma's game page remains unchanged
