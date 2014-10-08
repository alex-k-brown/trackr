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


# @api_view(('POST',))

def add_goal(request):
    request.DATA.update(request.DATA['value'])
    del request.DATA['value']

    errors = False

    # if request.method == 'PUT':
    #     response = ChildGoal.objects.get(pk=request.DATA['id'])
    #     serializer = ChildGoalSerializer(response, data=request.DATA)
    if request.method == 'POST':
        serializer = ChildGoalSerializer(data=request.DATA)

    # if serializer.is_valid():
    #     serializer.save()
    #     question_id = serializer.data['id']
    #
    #     check_calculation(serializer.data['survey'], serializer.data['company'], serializer.data['question'])
    # else:
    #     errors = True
    #     request.DATA['errors'] = serializer.errors
    if errors:
        return Response(request.DATA, status=status.HTTP_400_BAD_REQUEST)

        question = QuestionResponse.objects.get(pk=question_id)
    return Response(QuestionResponseReadSerializer(question).data)
