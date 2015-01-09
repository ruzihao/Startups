from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home_view(request):
	t = get_template('home.html')
	html = t.render(Context())
	return HttpResponse(html)
