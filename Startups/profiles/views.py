from django.shortcuts import render
from django.http import HttpResponse

import os.path


# Create your views here.
def profiles_view(request):
    # return HttpResponse(render(request, "profiles/company.html", {}))
    return HttpResponse(render(request, "profiles/company.html", {}))

def test_view(request):
    # if 'company' in request.GET.keys():
    return HttpResponse(render(request, "profiles/test.html", {}))