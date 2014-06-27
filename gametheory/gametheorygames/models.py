from django.db import models
from django.core.urlresolvers import reverse

class Game(models.Model):
	def get_absolute_url(self):
		return '%d/' % (self.id,)
