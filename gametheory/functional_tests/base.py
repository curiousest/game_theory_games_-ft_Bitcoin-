import sys, os
from django.contrib.staticfiles.testing import StaticLiveServerCase
from selenium import webdriver

class FunctionalTest(StaticLiveServerCase):

	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url
	
	
	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()


	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	
	def tearDown(self):
		self.browser.quit()

