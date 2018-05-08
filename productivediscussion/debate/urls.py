"""URL configuration for debate."""
from django.conf.urls import re_path
from debate.views import DebateDetailView, DebateCreateView

urlpatterns = [
    re_path(r'^create/$', DebateCreateView.as_view(), name='debate_create'),
    re_path('^(?P<pk>\d+)', DebateDetailView.as_view(), name='debate_detail'),
]
