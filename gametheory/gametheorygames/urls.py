from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^losing_game', 'gametheorygames.views.losing_game', name='losing_game'),
    url(r'^play_losing_game', 'gametheorygames.views.play_losing_game', name='play_losing_game'),
)
