import networkx as nx
import matplotlib.pyplot as plt


def draw(graph: nx.Graph):
    print("Nodes of graph: ")
    print(graph.nodes())
    print("Edges of graph: ")
    print(graph.edges())
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos=pos, with_labels=True)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.savefig("di_graph.png")
    plt.show()
