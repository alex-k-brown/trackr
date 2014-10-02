from models import *
from rest_framework import serializers


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal


class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame


class ChildGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildGoal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
