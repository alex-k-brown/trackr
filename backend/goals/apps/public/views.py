from django.shortcuts import render
from serializers import *
from rest_framework import generics

# Create your views here.


class GoalList(generics.ListCreateAPIView):
    model = Goal
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()


class AddGoal(generics.CreateAPIView):
    model = Goal
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
