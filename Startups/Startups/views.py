# coding: UTF-8

from django.shortcuts import render
from django.http import HttpResponse
from django import template

def hello_view(request):
	return HttpResponse(render(request, r"index.html", {}))
