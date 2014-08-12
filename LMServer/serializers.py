from django.contrib.auth.models import User, Group
from rest_framework import serializers
from LMServer.models import Event, LMUser
from django.db import models
import time, datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):

    fbUser = serializers.SerializerMethodField('createLMUser')
 
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    created = date

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'fbUser')

    def createLMUser(self, obj):
        #print "obj" + obj.username
        lm1 = LMUser(user=obj, fbUser="12345", created=UserSerializer.created)
        lm1.save()
        return lm1.fbUser



class LMUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LMUser
        fields = ('fbUser', 'twitterUser', 'googleUser', 'created')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'created', 'usersInvited', 'created')
