from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserTasksView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


def get_user_tasks(request, user_id=None):
    msg = "You submitted user_id : %d" % user_id
    response = HttpResponse(msg)
    return response