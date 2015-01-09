from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from profiles.models import company_ent, funding_ent
from django.db.models import Sum
import json


def profiles_view(request, cid):
     if len(cid) != 0:
          cid = int(cid)
     else:
          return HttpResponse("Hello, cid is missing.")

     #retrieve json for graph start here
     class node(object):
          def __init__(self, cid, name, match, description, invest_value):
               self.id = cid #indentified by cid
               self.name = name
               self.match = match
               self.description = description
               self.invest_value = invest_value
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
          else:
               invest_sum = 1000000 #default value 1M
          #add itself as a node
          graph.add_node(node(seed, company_ent.objects.get(pk=seed).name, 1, company_ent.objects.get(pk=seed).short_description, int(invest_sum[0].to_integral_value())))
               
          #add other nodes
          for investment in investments:
               graph.add_investment(seed, investment)

     #retrieve json for graph end here

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
     #retrieve json for graph start here
     
     t = get_template('profile.html')
     html = t.render(Context({'company':company_ent.objects.get(pk=cid), 'json': json.dumps(graph,default=object2dict)}))
     return HttpResponse(html)
