from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from profiles.models import company_ent, funding_ent, acquisition_ent, member_ent
from profiles import classes
from django.db.models import Sum
from time import strptime, localtime
import json


def profiles_view(request, cid):
     if len(cid) != 0:
          cid = int(cid)
     else:
          return HttpResponse("Hello, cid is missing.")

     #########################
     #retrieve json for graph start here
     def find_investments_by_cid(cid):
          return funding_ent.objects.filter(investors = company_ent.objects.get(pk=cid).name)

     def find_investors_by_cid(cid):
          return funding_ent.objects.filter(cid = cid)
		  
     def add_investment(graph, investor_cid, investment):
          invest_traget = company_ent.objects.get(pk=investment.cid.cid)
          #amount should be fixed by partners_count, match haven't been defined yet
          graph.add_node(invest_traget.cid, invest_traget.name, 1, invest_traget.short_description, float(investment.amount)) #decimal to float
          graph.add_edge(investor_cid, invest_traget.cid)

     graph = classes.graph()
     
     seed_list = [cid,]
     investors_funding = find_investors_by_cid(cid)
     
     for investor in investors_funding:
          seed_ent = company_ent.objects.filter(name = investor.investors)[:1]
          if len(seed_ent) != 0:
               seed_list.append(seed_ent[0].cid)
          
     seed_list = set(seed_list)
     
     for seed in seed_list:
          investments = find_investments_by_cid(seed)
          if len(investments) > 0:
               invest_sum = investments.aggregate(Sum("amount")).values()
               #add itself as a node
               graph.add_node(seed, company_ent.objects.get(pk=seed).name, 1, company_ent.objects.get(pk=seed).short_description, invest_sum)
          else:
               graph.add_node(seed, company_ent.objects.get(pk=seed).name, 1, company_ent.objects.get(pk=seed).short_description, 1000000) # default invest_sum 1M
               
          #add other nodes
          for investment in investments:
               add_investment(graph, seed, investment)

     
     #retrieve json for graph end here
     #########################

     #########################
     #retrieve json for timeline start here
     
     #Date reader for acquisition
     def read_date(string):
          string.strip()
          if string.startswith("Since "):
               string = string[len("Since "):]
          try:
               result = strptime(string, "%b-%Y")
          except ValueError, e:
               result = strptime(string, "%Y")
          return result

     timeline = classes.timeline(timeline_headline = "Milestones of %s" % company_ent.objects.get(pk=seed).name, timeline_text="with timeline display")

     #Establishment event
     query = company_ent.objects.get(pk=cid)
     if len(query.founded_on) != 0:
          event_date = read_date(query.founded_on)
          timeline.add_date(headline="Company founded in %s" % (event_date.tm_year), start_y = event_date.tm_year, start_m = event_date.tm_mon, end_y = event_date.tm_year, end_m = event_date.tm_mon)
		  
     #Funding events
     queryset = funding_ent.objects.filter(cid = cid)
     
     funding_event = {}
     for query in queryset:
          if query.series not in funding_event:
               funding_event[query.series] = [query.investors,]
          else:
               funding_event[query.series].append(query.investors)
               
     for round in funding_event:
          round_entity = queryset.filter(series=round)[0]
          event_date = read_date(round_entity.date)
          timeline.add_date(headline="Funding: (%s) $%s from %s" % (round,  format(round_entity.amount, ','), ",".join(funding_event[round])), start_y = event_date.tm_year, start_m = event_date.tm_mon, end_y = event_date.tm_year, end_m = event_date.tm_mon)

     #Acquisitions/investments events
     queryset = acquisition_ent.objects.filter(cid = cid)

     for query in queryset:
          event_date = read_date(query.since)
          timeline.add_date(headline="Invested in %s" % (query.name), start_y = event_date.tm_year, start_m = event_date.tm_mon, end_y = event_date.tm_year, end_m = event_date.tm_mon)

     #Member events
     queryset = member_ent.objects.filter(cid = cid).exclude(category="").exclude(since="")

     for query in queryset:
          event_date = read_date(query.since)
          timeline.add_date(headline="Appointed %s to %s:%s" % (query.name, query.category, query.title), start_y = event_date.tm_year, start_m = event_date.tm_mon, end_y = event_date.tm_year, end_m = event_date.tm_mon)

     #Check whether date_list is empty
     if len(timeline.get_date_list()) == 0:
          event_date = localtime()
          timeline.add_date(headline="No event recorded yet", start_y = event_date.tm_year, start_m = event_date.tm_mon, end_y = event_date.tm_year, end_m = event_date.tm_mon)


     #timeline.add_era(headline="default_era", start_y = 2010, end_y = 2012)

     #retrieve json for timeline end here
     ######################### 
     
     
     t = get_template('profile.html')
     html = t.render(Context({'company':company_ent.objects.get(pk=cid), 'json': json.dumps(graph.graph2dict()), 'timeline': json.dumps(timeline.timeline2dict())}))
     return HttpResponse(html)

	 
def company_list(request):
     company_list1 = company_ent.objects.filter(short_description = "Venture Capital")[0:10]
     company_list2 = company_ent.objects.filter(short_description = "Computer Software")[0:10]
     company_list3 = company_ent.objects.filter(short_description = "Internet Publishing and Broadcasting and Web Search Portals")[0:10]
     
     t = get_template('company_list.html')
     html = t.render(Context({"company_list1": company_list1, "company_list2": company_list2, "company_list3": company_list3}))
     return HttpResponse(html)
