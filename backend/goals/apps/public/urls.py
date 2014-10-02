
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings

urlpatterns = patterns(
    'apps.public.views',

    url(r'^goals/$', GoalList.as_view(), name='goal-list'),
    url(r'^goals/(?P<pk>[0-9]+)$', GoalDetail.as_view(), name='goal-details'),
    url(r'^add-goal/$', add_goal, name='add-goal')


)