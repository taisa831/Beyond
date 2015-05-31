# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from team.models import TeamGames, TeamGameFirstHalfScores, TeamGameSecondHalfScores, TeamGameInnings, TeamPlayers

def score_book(request, team_game_id=None):
    team_game = TeamGames.objects.get(pk=team_game_id)
    team_game_innings = TeamGameInnings.objects.filter(team_game_id__exact=team_game_id)
    first_half_scores = TeamGameFirstHalfScores.objects.filter(team_game_id__exact=team_game_id)
    second_half_scores = TeamGameSecondHalfScores.objects.filter(team_game_id__exact=team_game_id)
    return render_to_response('team/score_book.html',  # 使用するテンプレート
        {'first_half_scores': first_half_scores, 'second_half_scores': second_half_scores,'team_game_innings': team_game_innings ,'team_game': team_game},  # テンプレートに渡すデータ
        context_instance=RequestContext(request))  # その他標準のコンテキスト

def players(request):
    team_players = TeamPlayers.objects.filter(team_id__exact=1)
    return render_to_response('team/players.html',
        {'team_players': team_players},
        context_instance=RequestContext(request))