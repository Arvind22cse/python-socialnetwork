import networkx as nx
import matplotlib.pyplot as plt
def plot_density():
	x=[]
	y=[]
	for i in range (0,11):
		G=nx.read_gml('evolution_'+str(i)+'.gml')
		x.append(i)
		y.append(nx.density(G))
	plt.xlabel('Time')
	plt.ylabel('Density')
	plt.title('Change in Density')
	plt.plot(x,y)
	plt.show()
def obesity(G):
	num=0
	for each in G.nodes():
		if G.nodes[each]['name']==40:
			num+=1
	return num
def plot_obes():
	x=[]
	y=[]
	for i in range (0,11):
		G=nx.read_gml('evolution_'+str(i)+'.gml')
		x.append(i)
		y.append(obesity(G))
	plt.xlabel('Time')
	plt.ylabel('obesity')
	plt.title('Change in obesity')
	plt.plot(x,y)
	plt.show()

plot_density()
plot_obes()
