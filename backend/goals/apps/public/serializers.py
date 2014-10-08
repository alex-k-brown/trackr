from models import *
from rest_framework import serializers


class GoalSerializer(serializers.ModelSerializer):
    child_goals = serializers.SerializerMethodField('get_child_goals')

    class Meta:
        model = Goal
        depth = 1

    def get_child_goals(self, obj):
        children = obj.children.all()
        return ChildGoalSerializer(children, many=True).data



class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame


class ChildGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildGoal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
