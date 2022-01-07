from django.urls import path
from .views import *

urlpatterns = [
    path('', PieChartView.as_view()),
    path('dought/', DoughtChartView.as_view()),
]