from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from LMServer.serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    #model = User
    print "function called"
    """
    List all snippets, or create a new snippet.
    """

    if request.method == 'POST':
        print "login post request"
        print request.DATA
        return Response(request.DATA, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def signup(request):

    print "function called"
    """
    List all snippets, or create a new snippet.
    """

    if request.method == 'POST':
        userSerializer = UserSerializer(data=request.DATA)
        if userSerializer.is_valid():
            userSerializer.save()
            print "signup post request"
            print request.DATA

            # return authorization key to client


            return Response(request.DATA, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LMUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LMUser.objects.all()
    serializer_class = LMUserSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer