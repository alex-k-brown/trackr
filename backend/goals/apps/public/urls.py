
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings

urlpatterns = patterns(
    'apps.public.views',

    url(r'^goals/$', GoalList.as_view(), name='goal-list'),
    url(r'^goals/(?P<pk>[0-9]+)$', GoalDetail.as_view(), name='goal-details'),
    url(r'^add-goal/$', add_goal, name='add-goal'),
    url(r'^child-goals/$', ChildGoalList.as_view(), name='child-goals-list'),
    url(r'^child-goals/(?P<pk>[0-9]+)$', ChildGoalDetail.as_view(), name='child-goals-detail'),
    url(r'^time-frame/$', TimeFrameList.as_view(), name='time-frames-list')


)