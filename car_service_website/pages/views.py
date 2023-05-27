from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "pages/MainPage.html"

