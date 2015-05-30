from django.conf.urls import patterns, include, url
from baseball import views

urlpatterns = patterns('',
    url(r'^score_book/$', views.score_book, name='score_book'),
)
