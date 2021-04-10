import pandas as pd
import networkx as nx
DIMENSION = 60
MY_ID = 1
df = pd.read_csv('Social_Matrix.csv')
sociomatrix = df.values

undirected_graph = nx.DiGraph()
undirected_graph.add_nodes_from(range(1,DIMENSION+1))

for i in range(0, len(sociomatrix)):
    for j in range(0, len(sociomatrix[0])):
        if sociomatrix[i][j] == 1:
            undirected_graph.add_edge(i+1,j+1)

undirected_graph.in_degree(MY_ID)
undirected_graph.out_degree(MY_ID)
nx.closeness_centrality(undirected_graph,MY_ID)
nx.betweenness_centrality(undirected_graph)[MY_ID]

in_degree_value = undirected_graph.in_degree(MY_ID)
print('The in degree value is', in_degree_value)
out_degree_value = undirected_graph.out_degree(MY_ID)
print('The out degree value is', out_degree_value)
closeness_centralit_value = nx.closeness_centrality(undirected_graph,MY_ID)
print('The closeness centrality value is', closeness_centralit_value)
betweenness_centrality_value = nx.betweenness_centrality(undirected_graph)[MY_ID]
print('The betweenness centrality value is', betweenness_centrality_value)


