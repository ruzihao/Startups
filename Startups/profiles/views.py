from django.shortcuts import render
from django.http import HttpResponse

import os.path


# Create your views here.
def profiles_view(request):
    return HttpResponse(render(request, "profiles/home.html", {}))

def company_view(request):
    return HttpResponse(render(request, "profiles/company.html", {}))

def company_vidyo_view(request):
    return HttpResponse(render(request, "profiles/vidyo.html", {}))

# def test_view(request):
#     return HttpResponse(render(request, "profiles/test.html", {}))