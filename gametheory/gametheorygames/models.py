from django.db import models
from django.core.urlresolvers import reverse

GAME_STATES = {	"CREATED" : 0,
				"LIVE" : 1
		}

class Game(models.Model):
	state = models.IntegerField(default = GAME_STATES["CREATED"])
	
	def get_absolute_url(self):
		return '%d/' % (self.id,)
		
class LosingGame(Game):
	depositAddress = models.TextField(default='')
	
	def get_Coinbase_callback_url(self):
		return '%d/coinbase_callback/' % (self.id,)
