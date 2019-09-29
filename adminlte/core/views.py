from django.shortcuts import render
from django.views.generic.base import TemplateView

# DASHBOAR
class HomePageView(TemplateView):
    template_name = "core/index.html"

class HomePageView2(TemplateView):
    template_name = "core/index2.html"

# PAGES
class CalendarView(TemplateView):
    template_name = "core/pages/calendar.html"
