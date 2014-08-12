from django.contrib.auth.models import User, Group
from rest_framework import serializers
from LMServer.models import Event, UserProfile
from django.db import models
import time, datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):

    parseUser = serializers.SerializerMethodField('create_parse_user')
    fbUser = serializers.SerializerMethodField('create_user_profile')

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    user_profile_key = serializers.PrimaryKeyRelatedField()
    #print lmuser 
    created = date

    # parse account needs to be created and attached 

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password', 'parseUser', 'fbUser')

    def create_parse_user(self, obj):

        # get parse user here

        return "new parse user 123"

    def create_user_profile(self, obj):
        #print "obj" + obj.username
        profile = UserProfile(user=obj, parseUser="new_parse_user", fbUser="12345", created=UserSerializer.created)
        profile.save()
        return profile.fbUser 

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.PrimaryKeyRelatedField()

    # every user needs to be connected to a 
    # parse account for push notifications
    parseUser = serializers.CharField(required=True) 
    fbUser = serializers.CharField(required=False)
    #print user

    class Meta:
        model = UserProfile
        fields = ('user', 'parseUser', 'fbUser')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'created', 'usersInvited', 'created')
