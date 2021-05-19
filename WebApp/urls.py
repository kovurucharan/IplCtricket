
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('th/',views.THNQ),
    path('tm/',views.cricketteams),
    path('player/',views.PlayerHistory),
    path('tlist/',views.TeamList),
    path('plist/',views.Playerlist),
    path('matches/',views.MatchesHistory),
    path('pointlist/',views.pointstable),
    path('tmdetail/<int:id>/',views.teamdetail),
    path('pdetail/<int:id>/',views.playerdetail),
    path('playerdelete/<int:id>/',views.deleteplayer),
    path('teamplayers/<int:id>',views.TeamPlayers),
    path('kc/',views.KC),

]