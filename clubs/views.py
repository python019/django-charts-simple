from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club

class ClubChartView(TemplateView):
    template_name = 'clubs/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context
    