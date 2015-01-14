from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from profiles.models import company_ent, round_ent, investment_ent, acquisition_ent
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
          return investment_ent.objects.filter(investor_cid = cid)

     def find_investors_of_cid(cid):
		  round_id_list = round_ent.objects.filter(cid = cid).values_list("round_id")
		  return investment_ent.objects.filter(round_id__in =round_id_list).values_list("investor_cid")
		  
     def add_investment(graph, investor_cid, investment):
          invest_traget = investment.round_id.cid
          #amount should be fixed by partners_count, match haven't been defined yet
          graph.add_node(invest_traget.cid, invest_traget.name, 1, invest_traget.company_category_list, 1000000) #decimal to float; amount is not accurate
          graph.add_edge(investor_cid, invest_traget.cid)

     graph = classes.graph()
     
     seed_list = [cid, ]
     investors_of_cid = find_investors_of_cid(cid)

     if investors_of_cid is not None:
          for cid_tuple in investors_of_cid:
			seed_list.append(cid_tuple[0])
     seed_list = set(seed_list)
     
     for seed in seed_list:
          seed_company_ent =  company_ent.objects.get(pk=seed)
          investments = find_investments_by_cid(seed)
          if len(investments) > 0:
			   #compute the sum of money invested by certain company
			   round_list = round_ent.objects.filter(round_id__in = investments.values_list("round_id"))
			   invest_sum = round_list.aggregate(Sum("raised_amount_usd")).values()[0]           #amount is not accurate
			   #add itself as a node
			   graph.add_node(seed,seed_company_ent.name, 1, seed_company_ent.company_category_list, invest_sum)
          else:
			   graph.add_node(seed, seed_company_ent.name, 1, seed_company_ent.company_category_list, 1000000) # default invest_sum 1M
               
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

     query = company_ent.objects.get(pk=cid)
     timeline = classes.timeline(timeline_headline = "Milestones of %s" % query.name, timeline_text="with timeline display")

     #Establishment event
     if query.founded_at is not None:
          event_date = query.founded_at
          timeline.add_date(headline="Company founded in %s" % (event_date.year), start_y = event_date.year, start_m = event_date.month, end_y = event_date.year, end_m = event_date.month)
		  
     #Funding events
     queryset = investment_ent.objects.filter(round_id__in = round_ent.objects.filter(cid = cid))

     funding_event = {}
     for query in queryset:
          if query.round_id not in funding_event:
               funding_event[query.round_id] = [query.investor_cid.name,]
          else:
               funding_event[query.round_id].append(query.investor_cid.name)
               
     for round in funding_event:
          event_date = round.funded_at
          timeline.add_date(headline="Funding: (%s, %s) $%s from %s" % (round.funding_round_type, round.funding_round_code, format(round.raised_amount_usd, ','), ",".join(funding_event[round])), start_y = event_date.year, start_m = event_date.month, end_y = event_date.year, end_m = event_date.month)

     #Acquisitions events
     queryset = acquisition_ent.objects.filter(acquirer_cid = cid)

     for query in queryset:
          event_date = query.acquired_at
          timeline.add_date(headline="Acquided %s" % (query.target_cid.name), start_y = event_date.year, start_m = event_date.month, end_y = event_date.year, end_m = event_date.month)

     #Check whether date_list is empty
     if len(timeline.get_date_list()) == 0:
          event_date = localtime()
          timeline.add_date(headline="No event recorded yet", start_y = event_date.tm_year, start_m = event_date.tm_mon, end_y = event_date.tm_year, end_m = event_date.tm_mon)


     #timeline.add_era(headline="default_era", start_y = 2010, end_y = 2012)

     #retrieve json for timeline end here
     ######################### 
     
     
     t = get_template('profile.html')
     html = t.render(Context({'company':company_ent.objects.get(pk=cid), 'graph': json.dumps(graph.graph2dict()), 'timeline': json.dumps(timeline.timeline2dict())}))
     return HttpResponse(html)

	 
def company_list(request):
     company_list1 = company_ent.objects.filter(market = "Venture Capital")[0:10]
     company_list2 = company_ent.objects.filter(market = "Software")[0:10]
     company_list3 = company_ent.objects.filter(market = "Internet")[0:10]
     
     t = get_template('company_list.html')
     html = t.render(Context({"company_list1": company_list1, "company_list2": company_list2, "company_list3": company_list3}))
     return HttpResponse(html)
