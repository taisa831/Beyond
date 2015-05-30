# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from baseball.models import BaseballTeamGames, BaseballTeamGameTopScores, BaseballTeamGameBottomScores

def score_book(request):
    game = BaseballTeamGames.objects.get(pk=1)
    top_scores = BaseballTeamGameTopScores.objects.filter(team_game_id__exact=1)
    bottom_scores = BaseballTeamGameBottomScores.objects.filter(team_game_id__exact=1)
    return render_to_response('baseball/score_book.html',  # 使用するテンプレート
                              {'top_scores': top_scores, 'bottom_scores': bottom_scores, 'game': game},  # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト