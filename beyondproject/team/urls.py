from django.conf.urls import patterns, include, url
from team import views

urlpatterns = patterns('',
    url(r'^score_book/(?P<team_game_id>\d+)/$', views.score_book, name='score_book'),
    url(r'^players/$', views.players, name='players'),
)
