from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class= UserSerializer


class TaskViewSets(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated, IsOwnerOrReadOnly]





