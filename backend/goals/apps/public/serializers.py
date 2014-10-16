from models import *
from rest_framework import serializers
from datetime import date
from datetime import timedelta


class GoalSerializer(serializers.ModelSerializer):
    child_goals = serializers.SerializerMethodField('get_child_goals')
    goal_progress = serializers.SerializerMethodField('get_goal_progress')
    goal_time = serializers.SerializerMethodField('get_goal_time')

    class Meta:
        model = Goal
        depth = 1

    def get_child_goals(self, obj):
        children = obj.children.all()
        return ChildGoalSerializer(children, many=True).data

    def get_goal_progress(self, obj):
        children = obj.children.all()
        completed = children.filter(complete=True).count()
        total = children.count()
        if total==0:
            return 0       
        return {'done': round((float(completed)/total) * 100), 'total': total}

    def get_goal_time(self, obj):
        today = date.today()
        deadline = obj.dueDate
        dayspan = obj.timeFrame.days
        start = deadline - timedelta(days=dayspan)
        dayspassed = today - start
        return {'percentage': round((float(dayspassed.days) / dayspan) * 100), 'dayspassed': dayspassed}


class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame


class ChildGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildGoal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
