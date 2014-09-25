from models import *
from rest_framework import serializers


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal


