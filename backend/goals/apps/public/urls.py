from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('apps.public.views',
    url(r'^goals$', GoalList.as_view(), name='goal-list'),
)