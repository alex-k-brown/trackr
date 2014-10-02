
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings

urlpatterns = patterns(
    'apps.public.views',

    url(r'^goals/$', GoalList.as_view(), name='goal-list'),
    url(r'^add-goal/$', add_goal, name='add-goal')


)