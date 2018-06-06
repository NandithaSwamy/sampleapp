from django.conf.urls import include, url
from django.contrib import admin
from app.views import Sampleview

urlpatterns = [
   url(r'^$', Sampleview.as_view()),
   url(r'/(?P<row_id>.*)$', Sampleview.as_view()),
]

