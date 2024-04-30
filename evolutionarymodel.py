import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time

def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 101))
    return G

def assign_bmi(G):
    for each in G.nodes:
        G.nodes[each]['name'] = random.randint(15, 40)  # Assign random BMI
        G.nodes[each]['type'] = 'person'

def get_label(G):
    dict1={}
    for each in G.nodes():
    	dict1[each]=G.nodes[each]['name']
    return dict1

def visualize(G,t):
	time.sleep(1)
	dict1 = get_label(G) 
	nodesize = get_size(G)  
	color_array=get_color(G)
	nx.draw(G, labels=dict1, node_size=nodesize,node_color=color_array)
	plt.savefig('evolution.png')
	plt.clf()
	plt.cla()
	nx.write_gml(G,'evolution_'+str(t)+'.gml')

def get_size(G):
    array1 = []  
    for each in G.nodes:
    	if G.nodes[each]['type']=='person':
        	array1.append(G.nodes[each]['name'] *5) 
    	else:
          array1.append(1000) 
    return array1  
def get_foci_nodes():
	f=[]
	for each in G.nodes():
		if G.nodes[each]['type']=='foci':
			f.append(each)
	return f
def get_persons_nodes():
	p=[]
	for each in G.nodes():
		if G.nodes[each]['type']=='person':
			p.append(each)
	return p
def add_foci_nodes(G):
	
	n=G.number_of_nodes()
	i=n+1
	foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
	for j in range(0,5):
		G.add_node(i)
		G.nodes[i]['name']=foci_nodes[j]
		G.nodes[i]['type']='foci'
		i=i+1
def get_color(G):
	c=[]
	for each in G.nodes():
		if G.nodes[each]['type']=='person':
			if G.nodes[each]['name']==15:
				c.append('green')
			elif G.nodes[each]['name']==40:
				c.append('yellow')
			else:
				c.append('blue')
			    
		else:
			c.append('red')
    	
        	

	return c
def add_foci_edges():
		foci_nodes=get_foci_nodes()
		person_nodes=get_persons_nodes()
		for each in person_nodes:
			r=random.choice(foci_nodes)
			G.add_edge(each,r)
			
			

def homophily(G):
	pnodes=get_persons_nodes()
	for u in pnodes:
		for v in pnodes:
			if u!=v:
				dif=abs(G.nodes[u]['name']-G.nodes[v]['name'])
				p=float(1)/(dif+1000)
				r=random.uniform(0,1)
				if r<p:
					G.add_edge(u,v)

def cmn(u,v,G):
	nu=set(G.neighbors(u))
	nv=set(G.neighbors(v))
	return len(nu & nv)

def closure(G):
	array1=[]
	for u in G.nodes():
		for v in G.nodes():
			if u!=v and(G.nodes[u]['type']=='person' or G.nodes[v]['type']=='person'):
				k=cmn(u,v,G)
				p=1-math.pow((1-0.01),k)
				tmp=[]
				tmp.append(u)
				tmp.append(v)
				tmp.append(p)
				array1.append(tmp)
	for each in array1:
		u=each[0]
		v=each[1]
		p=each[2]
		r=random.uniform(0,1)
		if r<p:
			G.add_edge(u,v)
def change_bmi(G):
	fnodes=get_foci_nodes()
	for each in fnodes:
		if G.nodes[each]['name']=='eatout':
			for each1 in G.neighbors(each):
				if G.nodes[each1]['name']!=40:
					G.nodes[each1]['name']=G.nodes[each1]['name']+1
		if G.nodes[each]['name']=='gym':
			for each1 in G.neighbors(each):
				if G.nodes[each1]['name']!=15:
					G.nodes[each1]['name']=G.nodes[each1]['name']-1

G = create_graph()  
assign_bmi(G) 
add_foci_nodes(G)

add_foci_edges()
time.sleep(10)
t=0
visualize(G,t)
for t in range(0,10):
	#visualize(G, dict1, nodesize,color_array) 
	homophily(G)
	#visualize(G, dict1, nodesize,color_array) 
	closure(G)
	change_bmi(G)
	visualize(G,t+1) 
