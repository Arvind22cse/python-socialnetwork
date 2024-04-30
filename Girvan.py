import networkx as nx
import matplotlib.pyplot as plt
# Function to find the edge with the highest edge betweenness centrality
def edge_to_remove(G):
    # Calculate edge betweenness centrality
    dict1 = nx.edge_betweenness_centrality(G)
    
    # Sort the edges by their betweenness centrality in descending order
    list_of_tuples = list(dict1.items())
    list_of_tuples.sort(key=lambda x: x[1], reverse=True)
    
    # Return the edge with the highest betweenness centrality
    return list_of_tuples[0][0]

# Girvan-Newman community detection algorithm
def girvan(G):
    # Find the connected components
    c = list(nx.connected_components(G))
    l = len(c)
    
    print('The number of connected components are:', l)
    
    # While there's only one connected component, keep removing edges with highest betweenness centrality
    while l == 1:
        G.remove_edge(*edge_to_remove(G))
        
        # Recompute connected components
        c = list(nx.connected_components(G))
        l = len(c)
        
        print('The number of connected components are:', l)
    
    return c

# Test the Girvan-Newman algorithm with a barbell graph
G = nx.barbell_graph(5, 0)  # 5 nodes on each side, no connecting nodes
c = girvan(G)  # Find communities

# Print the nodes in each connected component
for component in c:
    print(component)
    print("----------------")
nx.draw(G)
plt.show()