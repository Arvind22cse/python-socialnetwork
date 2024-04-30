import networkx as networkx
def add_node(n):
	G=nx.Graph()
	G.add_nodes_from(range(n))
	return G