from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from companies.models import CbCompanies, CbInvestments, CbRounds
from django.http import Http404
from django.views import generic
import difflib

# Create your views here.
class DetailView(generic.DetailView):
    model = CbCompanies
    template_name = 'cbcompanies_detail.html'

def detail_view(request):
    if 'company' in request.GET:
        company_name = request.GET['company']
        all_names = [k['company_name'].lower() for k in CbCompanies.objects.values('company_name')]
        if not company_name in all_names:
            matched = difflib.get_close_matches(company_name, all_names, n=5, cutoff=0.5)
            response = HttpResponse(render(request, r'companies/index.html', {'list_companies': True, 'list_name': matched}))
        else:
            p = get_object_or_404(CbCompanies, company_name=company_name)
            i = get_list_or_404(CbInvestments, company_name=company_name)
            r = get_list_or_404(CbRounds, company_name=company_name)
            response = HttpResponse(render(request, r'companies/detail.html', {'p': p, 'i': i, 'r': r}))
    else:
        context = {'name': ""}
        response = HttpResponse(render(request, r'companies/detail.html', context))
    return response

def index_view(request):
    return HttpResponse(render(request, r'companies/index.html',{}))

def index2_view(request):
    return HttpResponse(render(request, r'companies/index2.html',{}))

def analysis_view(request):
    return HttpResponse(render(request, r'companies/analysis.html',{}))

def analysis2_view(request):
    return HttpResponse(render(request, r'companies/analysis2.html',{}))
