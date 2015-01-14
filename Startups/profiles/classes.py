from profiles.obj2dict import object2dict

class graph(object):
	class node(object):
	  def __init__(self, cid, name, match, description, invest_value):
		   self.id = cid #indentified by cid
		   self.name = name
		   self.match = match
		   self.description = description
		   self.invest_value = invest_value
		   self.url = "/profiles/%d" % cid
	  def update_invest_value(self, increment):
		   self.invest_value += increment
	  def __repr__(self):
		   return "Node %s with id %d<br>" % (self.name, self.id)

	class edge(object):
	  def __init__(self, source_cid, target_cid):
		   self.source = source_cid   #indentified by cid
		   self.target = target_cid   #indentified by cid
	  def get_source(self):
		   return self.source
	  def get_target(self):
		   return self.target
	  def __repr__(self):
		   return "Link from %d to %d<br>" % (self.source, self.target)

	def __init__(self):
	   self.nodes = []
	   self.node_id_list = []
	   self.links = []

	def is_node_exist(self, new_node):
	   return new_node.id in self.node_id_list

	def is_edge_exist(self, new_edge):
	   for link in self.links:
			if link.source == new_edge.source and link.target == new_edge.target:
				 return True
	   else:
			return False

	def add_node(self, cid, name, match, description, invest_value):
	   new_node = graph.node(cid, name, match, description, invest_value)
	   if not self.is_node_exist(new_node):
			self.nodes.append(new_node)
			self.node_id_list.append(new_node.id)
	   else:
			index = self.node_id_list.index(cid)
			self.nodes[index].update_invest_value(invest_value)

	def add_edge(self, source_cid, target_cid):
	   new_edge = graph.edge(source_cid, target_cid)
	   if not self.is_edge_exist(new_edge):
			self.links.append(new_edge)
			
	def get_nodes(self):
	   return self.nodes

	def get_edges(self):
	   return self.links

	def get_node_id_list(self):
	   return self.node_id_list

	def del_node_by_ids(self, nodes):
	   if type(nodes) is not list: nodes = [ nodes ]
	
	   for node_id in nodes:
			index = self.node_id_list.index(node_id)
			#delete the node
			self.node_id_list.pop(index)
			self.nodes.pop(index)
	   
	   #delete related links
	   count = 0
	   indexes = []
	   for link in self.links:
			if link.get_source() in nodes or link.get_target() in nodes:
				indexes.append(count)
			count += 1
	   count = 0
	   for index in indexes:
			self.links.pop(index-count)    # offset
			count += 1
				   
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
	   for node in self.get_nodes():
			graph_dict["nodes"].append(object2dict(node))
	   for link in self.get_edges():
			graph_dict["links"].append(object2dict(link))
	   return graph_dict
	   
	  

class timeline(object):
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
		   super(timeline.event, self).__init__(headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d)
		   self.classname = classname
		   self.asset = {
						  "media": media,
						  "thumbnail": thumbnail,
						  "credit": credit,
						  "caption": caption,
						}
						
	def __init__(self, timeline_headline, timeline_type="default", timeline_text="", timeline_media="", timeline_credit="", timeline_caption=""):
	   self.headline = timeline_headline
	   self.type = timeline_type
	   self.text = "<p>%s</p>" % timeline_text
	   self.asset = {
								"media": timeline_media,
								"credit": timeline_credit,
								"caption": timeline_caption,
							  }
	   self.date_list = []
	   self.era_list = []

	def get_date_list(self):
	   return self.date_list
	   
	def get_era_list(self):
	   return self.era_list
	   
	def add_date(self, headline, start_y, start_m=1, start_d=1, end_y="", end_m=1, end_d=1, text="", tag="", classname="", media="", thumbnail="", credit="", caption=""):
	   self.date_list.append(self.event(headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d, classname, media, thumbnail, credit, caption))
	   
	def add_era(self, headline, start_y, start_m=1, start_d=1, end_y="", end_m=1, end_d=1, text="", tag=""):
	   self.era_list.append(self.era(headline, text, tag, start_y, start_m, start_d, end_y, end_m, end_d))
	   
	def timeline2dict(self):
	   timeline_dict = {"headline": self.headline,
						"type": self.type,
						"text": self.text,
						"asset": self.asset,
						"date":[],
						"era":[]}
	   for date in self.get_date_list():
			timeline_dict["date"].append(object2dict(date))
	   for era in self.get_era_list():
			timeline_dict["era"].append(object2dict(era))
	   return {"timeline": timeline_dict}