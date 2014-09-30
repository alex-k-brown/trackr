from django.shortcuts import render
from serializers import *
from rest_framework import generics

# Create your views here.


class GoalList(generics.ListCreateAPIView):
    model = Goal
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()


class EditGoal(generics.RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()


class Journal(generics.ListCreateAPIView):
    model = Journal
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()
