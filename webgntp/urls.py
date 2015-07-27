import webgntp.views
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', webgntp.views.GrowlForward.as_view()),
)
