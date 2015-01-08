from django.shortcuts import render
from django.http import HttpResponse
from django import template

def home_view(request):
	return HttpResponse(render(request, r"profiles/home.html", {}))
