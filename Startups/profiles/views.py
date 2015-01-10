from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from profiles.models import company_ent, funding_ent, acquisition_ent, member_ent
from django.db.models import Sum
from time import strptime
import json


def profiles_view(request, cid):
     if len(cid) != 0:
          cid = int(cid)
     else:
          return HttpResponse("Hello, cid is missing.")

     #########################
     #retrieve json for graph start here
     class node(object):
          def __init__(self, cid, name, match, description, invest_value):
               self.id = cid #indentified by cid
               self.name = name
               self.match = match
               self.description = description
               self.invest_value = invest_value
               self.url = "/profiles/%d" % cid
          def __repr__(self):
               return "Node %s with id %d<br>" % (self.name, self.id)

     class edge(object):
          def __init__(self, source_cid, target_cid):
               self.source = source_cid   #indentified by cid
               self.target = target_cid   #indentified by cid
          def __repr__(self):
               return "Link from %d to %d<br>" % (self.source, self.target)

     class graph(object):
          def __init__(self):
               self.nodes = []
               self.nodes_id = []
               self.links = []

          def is_node_exist(self, new_node):
               return new_node.id in self.nodes_id

          def is_edge_exist(self, new_edge):
               for link in self.links:
                    if link.source == new_edge.source and link.target == new_edge.target:
                         return True
               else:
                    return False

          def add_node(self, new_node):
               if not self.is_node_exist(new_node):
                    self.nodes.append(new_node)
                    self.nodes_id.append(new_node.id)

          def add_edge(self, new_edge):
               if not self.is_edge_exist(new_edge):
                    self.links.append(new_edge)
                    
          def get_nodes(self):
               return self.nodes

          def get_edges(self):
               return self.links
                    
          def add_investment(self, investor_cid, investment):
               invest_traget = company_ent.objects.get(pk=investment.cid.cid)
               #amount should be fixed by partners_count, match haven't been defined yet
               self.add_node(node(invest_traget.cid, invest_traget.name, 1, invest_traget.short_description, float(investment.amount))) #decimal to float
               self.add_edge(edge(investor_cid, invest_traget.cid))

          def __repr__(self):
               message = []
               message.append("Nodes<br>")
               for node in self.nodes:
                    message.append(str(node))
               message.append("Links<br>")
               for link in self.links:
                    message.append(str(link))
               return "".join(message)

          def graph2dict(self):
               graph_dict = {"nodes":[], "links":[]}
               for node in graph.get_nodes():
                    graph_dict["nodes"].append(object2dict(node))
               for link in graph.get_edges():
                    graph_dict["links"].append(object2dict(link))
               return graph_dict


     def find_investments_by_cid(cid):
          return funding_ent.objects.filter(investors = company_ent.objects.get(pk=cid).name)

     def find_investors_by_cid(cid):
          return funding_ent.objects.filter(cid = cid)

     graph = graph()
     
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
               graph.add_node(node(seed, company_ent.objects.get(pk=seed).name, 1, company_ent.objects.get(pk=seed).short_description, invest_sum))
          else:
               graph.add_node(node(seed, company_ent.objects.get(pk=seed).name, 1, company_ent.objects.get(pk=seed).short_description, 1000000)) # default invest_sum 1M
               
          #add other nodes
          for investment in investments:
               graph.add_investment(seed, investment)

     
     #retrieve json for graph end here
     #########################

     #########################
     #retrieve json for timeline start here

     class era(object):
          def __init__(self, headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d):
               self.startDate = "%d,%d,%d" % (start_y, start_m, start_d)
               if end_y == "":
                    self.endDate=",,,"
               else:
                    self.endDate = "%d,%d,%d" % (end_y, end_m, end_d)
               self.headline = headline
               self.text = "<p>%s</p>" % text
               self.tag = tag

     class event(era):
          def __init__(self, headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d, classname, media, thumbnail, credit, caption):
               super(event, self).__init__(headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d)
               self.classname = classname
               self.asset = {
                              "media": media,
                              "thumbnail": thumbnail,
                              "credit": credit,
                              "caption": caption,
                            }

     class timeline(object):
          def __init__(self, timeline_headline, timeline_type="default", timeline_text="", timeline_media="", timeline_credit="", timeline_caption=""):
               self.headline = timeline_headline
               self.type = timeline_type
               self.text = "<p>%s</p>" % timeline_text
               self.asset = {
                                        "media": timeline_media,
                                        "credit": timeline_credit,
                                        "caption": timeline_caption,
                                      }
               self.date = []
               self.era = []

          def add_date(self, headline, start_y, start_m=1, start_d=1, end_y="", end_m=1, end_d=1, text="", tag="", classname="", media="", thumbnail="", credit="", caption=""):
               self.date.append(event(headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d, classname, media, thumbnail, credit, caption))
               
          def add_era(self, headline, start_y, start_m=1, start_d=1, end_y="", end_m=1, end_d=1, text="", tag=""):
               self.era.append(era(headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d))
               
          def timeline2dict(self):
               timeline_dict = object2dict(timeline)
               return {"timeline": timeline_dict}

     timeline = timeline(timeline_headline = "Milestones of %s" % company_ent.objects.get(pk=seed).name, timeline_text="with timeline display")
     
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


     #timeline.add_era(headline="default_era", start_y = 2010, end_y = 2012)

     #retrieve json for timeline end here
     ######################### 

     def object2dict(obj):
          #convert object to a dict
          d = {}
          #d['__class__'] = obj.__class__.__name__
          #d['__module__'] = obj.__module__
          d.update(obj.__dict__)
          return d

##     def dict2object(d):
##          #convert dict to object
##          if'__class__' in d:
##               class_name = d.pop('__class__')
##               module_name = d.pop('__module__')
##               module = __import__(module_name)
##               class_ = getattr(module,class_name)
##               args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
##               inst = class_(**args) #create new instance
##          else:
##               inst = d
##          return inst
     
     
     t = get_template('profile.html')
     html = t.render(Context({'company':company_ent.objects.get(pk=cid), 'json': json.dumps(graph,default=object2dict), 'timeline': json.dumps(timeline.timeline2dict(),default=object2dict)}))
     return HttpResponse(html)

	 
def company_list(request):
     company_list1 = company_ent.objects.filter(short_description = "Venture Capital")[0:10]
     company_list2 = company_ent.objects.filter(short_description = "Computer Software")[0:10]
     company_list3 = company_ent.objects.filter(short_description = "Internet Publishing and Broadcasting and Web Search Portals")[0:10]
     
     t = get_template('company_list.html')
     html = t.render(Context({"company_list1": company_list1, "company_list2": company_list2, "company_list3": company_list3}))
     return HttpResponse(html)
