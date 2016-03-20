import webgntp.views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', webgntp.views.GrowlForward.as_view()),
]
