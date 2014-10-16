from django.shortcuts import render
from serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class GoalList(generics.ListCreateAPIView):
    model = Goal
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()


class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()


class ChildGoalDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ChildGoal
    serializer_class = ChildGoalSerializer
    queryset = ChildGoal.objects.all()


class ChildGoalList(generics.ListCreateAPIView):
    model = ChildGoal
    serializer_class = ChildGoalSerializer
    queryset = ChildGoal.objects.all()


class Journal(generics.ListCreateAPIView):
    model = Journal
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()


class TimeFrameList(generics.ListAPIView):
    model = TimeFrame
    serializer_class = TimeFrameSerializer
    queryset = TimeFrame.objects.all()


@api_view(('POST',))
def add_goal(request):
    errors = False

    if request.method == 'POST':
        goal_serializer = GoalSerializer(data=request.DATA)

        if goal_serializer.is_valid():
            goal = goal_serializer.save()
        else:
            errors = goal_serializer.errors

        if not errors:
            child_goal_steps = request.DATA.get('childGoals')

            for child_goal_step in child_goal_steps:
                child_goal = {
                    'step': child_goal_step,
                    'goal': goal.id,
                    'timeFrame': TimeFrame.objects.all()[0].id
                }

                child_goal_serializer = ChildGoalSerializer(data=child_goal)

                if child_goal_serializer.is_valid():
                    child_goal_serializer.save()
                else:
                    errors = child_goal_serializer.errors

    if errors:
        return Response(request.DATA, status=status.HTTP_400_BAD_REQUEST)

    saved_goal = Goal.objects.get(pk=goal.id)
    return Response(GoalSerializer(saved_goal).data)
