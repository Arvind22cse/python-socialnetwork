import networkx as nx
import itertools

def communities_brute(G):
    nodes = list(G.nodes())
    n = G.number_of_nodes()
    first_community = []
    
    # Generate all possible first communities
    for i in range(1, n // 2 + 1):
        comb = [list(x) for x in itertools.combinations(nodes, i)]
        first_community.extend(comb)

    # Generate second communities by finding complement
    second_community = []
    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community[i]))
        second_community.append(l)
    
    # Calculate intra-community edges and inter-community edges
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = []  # ratio of number of intra-community to inter-community edges
    
    # Calculate intra-community edges for first communities
    for i in range(len(first_community)):
        num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())
    
    # Calculate intra-community edges for second communities
    for i in range(len(second_community)):
        num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())
    
    # Calculate inter-community edges
    e = G.number_of_edges()
    for i in range(len(first_community)):
        num_inter_edges.append(e - num_intra_edges1[i] - num_intra_edges2[i])
    
    # Calculate the ratio of intra-community edges to inter-community edges
    for i in range(len(first_community)):
        ratio.append((num_intra_edges1[i] + num_intra_edges2[i]) / num_inter_edges[i])
    
    # Find the best division with the maximum ratio
    maxvalue = max(ratio)
    maxindex = ratio.index(maxvalue)
    
    print(f"({first_community[maxindex]},),({second_community[maxindex]},)")

# Create a barbell graph and find the best communities
G = nx.barbell_graph(5, 0)
communities_brute(G)
