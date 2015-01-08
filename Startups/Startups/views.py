from django.shortcuts import render
from django.http import HttpResponse
from django import template

def index_view(request):
	t = get_template('home.html')
	html = t.render()
	return HttpResponse(html)
