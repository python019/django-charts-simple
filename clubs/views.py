from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club

class PieChartView(TemplateView):
    template_name = 'clubs/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context
    
class DoughtChartView(TemplateView):
    template_name = 'clubs/dought_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context

class RadarChartView(TemplateView):
    template_name = 'clubs/radar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context
    