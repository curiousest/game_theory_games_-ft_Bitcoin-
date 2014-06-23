from .base import FunctionalTest
from selenium import webdriver
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
		
		# She sees an address to send BTC to
		# She sees the amount that she has to send to that address
		# She sends BTC to that address
		# She went to a different page to send BTC. She returns to her special URL to continue playing. 
		# She is congratulated for playing 
		
		self.fail("finish the test")
