from django.conf.urls import patterns, include, url
# from apps.public.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    # 'apps.public.views',

    # url(r'^goals/$', GoalList.as_view(), name='goal-list'),
    url(r'^', include('apps.public.urls')),
    # url(r'^goals$', GoalList.as_view(), name='goal-list'),
    url(r'^admin/', include(admin.site.urls)),
)
