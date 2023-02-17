from django.shortcuts import render

from django.views.generic import TemplateView

class BoardView(TemplateView):
    template_name = 'board/board.html'
