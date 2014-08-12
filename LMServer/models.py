from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Event(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	
	usersInvited = models.TextField()
	usersInvitedStatus = models.TextField()

	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'events'

class LMUser(models.Model):
	user = models.OneToOneField(User, primary_key=True)

	username = models.CharField(max_length=25)

	fbUser = models.CharField(max_length=100)
	#twitterUser = models.CharField(max_length=100)
	#googleUser = models.CharField(max_length=100)

	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'lmusers'

	def __unicode__(self, user, fbUser):
		self.user = user
		self.fbUser = fbUser
