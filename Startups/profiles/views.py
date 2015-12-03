from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from profiles.models import Company_ent, Funding_ent, Funding_round_ent, Acquisition_ent, Similar_objects_ent, Recommended_objects_ent
from django.db.models import Sum
from django.db import connection, transaction
from time import strptime
import json
import numpy as np
import pickle
import time


## read model
from PMF import PMF
def load_model():
	with open('./profiles/pmf/pmf.model') as f:
	    pmf = pickle.load(f)
	return pmf

pmf = load_model()

## read dict
dataPath = '/home/adamzjw/Desktop/Startups/profiles/pmf/'
with open(dataPath + "invID.json") as f:
	prem2invID = json.loads(f.read(), encoding="latin-1")

with open(dataPath + "tarID.json") as f:
	comDict = json.loads(f.read(), encoding="latin-1")

# inverse dictionarys
tarID2perm = {v: k for k, v in comDict.items()}

perm2cid = Company_ent.objects.all().values_list('company_permalink', 'cid')
perm2cid = {perm: cid for (perm, cid) in perm2cid}

# read end

def profiles_view(request, cid):
     if len(cid) != 0:
          cid = int(cid)
     else:
          return HttpResponse("Error, cid is missing.")

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
               self.root_id = None

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
                    
          def add_investment(self, investor, investment):
               invest_traget = investment.round_id.cid
               roundOfInvestment = investment.round_id
               amountOfInvestment = 1.0 * roundOfInvestment.raised_amount_usd / roundOfInvestment.funding_round.count()
               
               self.add_node(node(invest_traget.cid, invest_traget.name, 1, invest_traget.market, amountOfInvestment))
               self.add_edge(edge(investor.cid, invest_traget.cid))

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
               # haven't used
               graph_dict = {"nodes":[], "links":[]}
               for node in graph.get_nodes():
                    graph_dict["nodes"].append(object2dict(node))
               for link in graph.get_edges():
                    graph_dict["links"].append(object2dict(link))
               return graph_dict

     def investments_involved(investor):
          return investor.investor_company.all()

     def find_investors_by_cid(cid):
          funding_event =  Funding_ent.objects.filter(round_id__cid__cid=cid)
          return map(lambda x: x.investor_cid, funding_event)

     graph = graph()
     graph.root_id = cid
     
     seed_list = set(([Company_ent.objects.get(pk=cid),] + find_investors_by_cid(cid)))
     
     for seed in seed_list:
          investmentsOfSeed = investments_involved(seed).all().prefetch_related('round_id', 'round_id__cid', 'round_id__funding_round')
          totalCapitalOfSeed = 0

          for investment in investmentsOfSeed:
               roundOfInvestment = investment.round_id
               totalCapitalOfSeed += 1.0 * roundOfInvestment.raised_amount_usd / len(roundOfInvestment.funding_round.all())

          if totalCapitalOfSeed == 0:
               # default invest_sum 1M
               totalCapitalOfSeed = 1000000

          #add itself as a node
          graph.add_node(node(seed.cid, seed.name, 1, seed.market, totalCapitalOfSeed))
               
          #add other nodes
          for investment in investmentsOfSeed:
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

     timeline = timeline(timeline_headline = "Milestones of %s" % Company_ent.objects.get(pk=cid).name, timeline_text="with timeline display")

     #Funding round events
     funding_rounds = Funding_round_ent.objects.filter(cid = cid).prefetch_related('funding_round')
     
     funding_event = {}
     for _round in funding_rounds:
          round_type = _round.funding_round_type+_round.funding_round_code
          event_date = _round.funded_at
          investors_in_round = ",".join(map(lambda x: x.investor_cid.name, _round.funding_round.all()))
          timeline.add_date(headline="Funding: (%s) $%s from %s" % (round_type,  format(_round.raised_amount_usd, ','), investors_in_round), start_y = event_date.year, start_m = event_date.month, end_y = event_date.year, end_m = event_date.month)

     #Acquisitions/investments events
     queryset = Acquisition_ent.objects.filter(acquirer_cid = cid).select_related('target_cid')

     for query in queryset:
          event_date = query.acquired_at
          if query.price_amount > 0:
               timeline.add_date(headline="Invested in %s (%s %s)" % (query.target_cid.name, query.price_currency_code, format(query.price_amount, ',')), start_y = event_date.year, start_m = event_date.month, end_y = event_date.year, end_m = event_date.month)
          else:
               timeline.add_date(headline="Invested in %s" % (query.target_cid.name), start_y = event_date.year, start_m = event_date.month, end_y = event_date.year, end_m = event_date.month)


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

     # sim_rec fecth
     simObjs = list(Similar_objects_ent.objects.filter(cid=cid).order_by('score').select_related('counterpart'))
     recObjs = list(Recommended_objects_ent.objects.filter(cid=cid).order_by('-score').select_related('counterpart'))
     num_row = max(len(simObjs), len(recObjs))

     while len(simObjs) < num_row:
          simObjs.append(None)
     while len(recObjs) < num_row:
          recObjs.append(None)

     rowDict = []
     for i in range(num_row):
          if simObjs[i]:
               sim = {'obj':simObjs[i].counterpart, 'score':simObjs[i].score}
          else:
               sim = {'obj': {}, 'score':""}

          if recObjs[i]:
               rec = {'obj': recObjs[i].counterpart, 'score':recObjs[i].score}
          else:
               rec = {'obj': {}, 'score':""}
          
          rowDict.append({'sim': sim,
                          'rec': rec})


     
     side_info = {}

     company_ent = Company_ent.objects.get(pk=cid)
     if company_ent.stock_market is None:
          last_funding_round = Funding_round_ent.objects.filter(cid=cid).order_by('-funded_at')[:1]
          for _round in last_funding_round:
               side_info["current_round"] = _round.funding_round_type + _round.funding_round_code
     else:
          side_info["current_round"] = company_ent.stock_market

     side_info["numOfInvestors"] = len(Funding_ent.objects.filter(round_id__cid__cid=cid).all())

     t = get_template('profile.html')
     html = t.render(Context({'company':company_ent, 'Sim_Rec_Table':rowDict, 'side_info': side_info, 'json': json.dumps(graph,default=object2dict), 'timeline': json.dumps(timeline.timeline2dict(),default=object2dict)}))
     return HttpResponse(html)

	 
def company_list(request):
     company_list1 = Funding_ent.investor_cid.get_queryset().order_by('?')[:10]
     company_list2 = Company_ent.objects.filter(market = "Technology").order_by('?')[:10]
     company_list3 = Company_ent.objects.filter(market = "Health and Wellness").order_by('?')[:10]
     
     t = get_template('company_list.html')
     html = t.render(Context({"company_list1": company_list1, "company_list2": company_list2, "company_list3": company_list3}))
     return HttpResponse(html)

def search(request, search_string):
     if len(search_string) == 0:
          return HttpResponse("Error, search text is missing.")
     else:
          search_string.replace(" ", "_")

     search_result = Company_ent.objects.filter(name__icontains=search_string).all()[:10]
     
     t = get_template('search_result.html')
     html = t.render(Context({"search_result": search_result, "result_length": len(search_result), "search_string": search_string}))
     return HttpResponse(html)

def dataImport(request, param):
     if len(param) == 0:
          return HttpResponse("Error, search text is missing.")
     
     cursor = connection.cursor()

     if param == 'sim':
          cursor.execute("TRUNCATE TABLE `profiles_similar_objects_ent`")

     if param == 'rec':
          cursor.execute("TRUNCATE TABLE `profiles_recommended_objects_ent`")
     
     dataPath = '/home/adamzjw/Desktop/Startups/profiles/pmf/'

     with open(dataPath + "invID.json") as f:
          invDict = json.loads(f.read(), encoding="latin-1")

     with open(dataPath + "tarID.json") as f:
          comDict = json.loads(f.read(), encoding="latin-1")
          

     # if the company had accept investment, we won't regards it as a investor in the future
     com_perm_collection = comDict.keys()
     invDict = {k: v for k, v in invDict.items() if k not in com_perm_collection}

     # inverse dictionarys
     invDict = {v: k for k, v in invDict.items()}
     comDict = {v: k for k, v in comDict.items()}

     perm2cid = Company_ent.objects.all().values_list('company_permalink', 'cid')
     perm2cid = {perm: cid for (perm, cid) in perm2cid}

     if param == 'sim':
          with open(dataPath + 'knn_C.np') as f:
               knn_C = np.load(f)
          with open(dataPath + 'knn_I.np') as f:
               knn_I = np.load(f)

     if param == 'rec':
          with open(dataPath + 'rec_C.np') as f:
               rec_C = np.load(f)
          with open(dataPath + 'rec_I.np') as f:
               rec_I = np.load(f)


     def importObjs(knn_vec, Entry, id2perm_seed, id2perm_cp=None):
          if id2perm_cp is None:
               id2perm_cp = id2perm_seed
          objList = []
          for i in range(knn_vec.shape[0]):
               if i % 10000 == 0:
                    print "%d scanned" % i

               seed_pk = perm2cid.get(id2perm_seed.get(knn_vec[i,0], None), None)
               if seed_pk is None: continue
               seed = Company_ent.objects.get(pk=seed_pk) 

               cp_pk = perm2cid.get(id2perm_cp.get(knn_vec[i, 1], None), None)
               if cp_pk is None: continue
               counterpart = Company_ent.objects.get(pk=cp_pk)

               score = knn_vec[i, 2]

               toInsert = Entry(cid=seed, score=score, counterpart=counterpart)
               objList.append(toInsert)
          with transaction.atomic():
               Entry.objects.bulk_create(objList)

     if param == 'sim':
          importObjs(knn_C, Similar_objects_ent, id2perm_seed=comDict)
          importObjs(knn_I, Similar_objects_ent, id2perm_seed=invDict)

     if param == 'rec':
          importObjs(rec_C, Recommended_objects_ent, id2perm_seed=comDict , id2perm_cp=invDict)
          importObjs(rec_I, Recommended_objects_ent, id2perm_seed=invDict , id2perm_cp=comDict)

     return HttpResponse("Successfully Imported.")


def predict(request, cid):
     start_time = time.time()
     if len(cid) == 0:
          return HttpResponse("Error, cid is missing.")

     investor = Company_ent.objects.get(pk=cid)
     invID = prem2invID.get(investor.company_permalink, None)

     if invID is None:
     	return HttpResponse("This company haven't had any investment disclosures.")

     pred = pmf.predict(invID)
     pred_score = np.sort(pred)[-20:]
     pred_invID = np.argsort(pred)[-50:]
     pred_cid = map(lambda x: perm2cid.get(tarID2perm.get(x, None), None), pred_invID)
     pred_comEnt = map(lambda x: Company_ent.objects.get(pk=x), pred_cid)

     running_time = "%s seconds" % (time.time() - start_time)

     t = get_template('predict_result.html')
     html = t.render(Context({"investor": investor, "pred": zip(pred_comEnt, pred_score), "running_time": str(running_time)}))
     return HttpResponse(html)