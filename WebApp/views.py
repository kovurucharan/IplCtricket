from django.shortcuts import render, redirect
from .forms import TeamForm, PlayerForm, MatchesForm,StatisticsForm
from WebApp.models import Team, Player, Statistics
import datetime
from datetime import datetime
from django.http import HttpResponseRedirect
from itertools import combinations
from django.http import HttpResponse
import random


def THNQ(request):
    return render(request, 'MyApp/thanks.html')


def Home(request):
    return render(request, 'MyApp/home.html')


def cricketteams(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tlist/')
    else:
        form = TeamForm()
    return render(request, 'MyApp/teams.html', {'form': form})


def TeamList(request):
    obj = Team.objects.all()
    return render(request, 'MyApp/teamlist.html', {'obj': obj})

def teamdetail(request,id=None):
    rk=Team.objects.get(id=id)
    return render(request,'MyApp/tmdetail.html',{'rk':rk})



def PlayerHistory(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/plist/')
    else:
        form = PlayerForm()
    return render(request, 'MyApp/player.html', {'form': form})



def Playerlist(request):
    obj = Player.objects.all()
    return render(request, 'Myapp/playerlist.html', {'obj': obj})

def playerdetail(request,id=None):
    sk=Player.objects.get(id=id)
    return render(request,'MyApp/playerdetail.html',{'sk':sk})


def MatchesHistory(request):
    teams = Team.objects.all()
    team1 = random.choice(teams)
    var = teams.exclude(tname=team1.tname)
    team2 = random.choice(var)
    winner = random.choice((team1, team2))

    jk, flag = Statistics.objects.get_or_create(team=winner)
    jk.playing_matches += 1
    jk.win += 1
    jk.points += 2
    jk.save()
    if team1.tname==jk.team.tname:
        kl=team2
    else:
        kl=team1
    kc,flag=Statistics.objects.get_or_create(team=kl)
    kc.playing_matches += 1
    kc.loss += 1
    kc.points += 0
    kc.save()
        # print(winner)
        # print(team1, team2)
        # print(type(team2))

    return render(request, 'MyApp/matches.html', {'team1': jk,'team2':kc})


# def Points(request):
#     if request.method == 'POST':
#         form =StatisticsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/th/')
#     else:
#         form = StatisticsForm()
#     return render(request, 'MyApp/point.html', {'form': form})

def pointstable(request):
    obj=Statistics.objects.all()
    return render(request,'MyApp/points.html',{'obj':obj})



def deleteplayer(request,id=None):
    Player.objects.get(id=id).delete()
    return HttpResponseRedirect('/plist/')

def TeamPlayers(request,id=None):
    teams=Team.objects.get(id=id)
    players=Player.objects.filter(team=teams)
    return render(request,'MyApp/teamplayers.html',{'team':teams,'players':players})















