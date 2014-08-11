from django.contrib.auth.models import User, Group
from rest_framework import serializers
from LMServer.models import Event, LMUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class LMUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LMUser
        fields = ('url', 'username', 'fbUser', 'twitterUser', 'googleUser', 'created')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'created', 'usersInvited', 'created')