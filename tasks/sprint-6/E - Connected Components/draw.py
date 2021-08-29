import networkx as nx
import matplotlib.pyplot as plt


def draw(graph: nx.Graph):
    print("Nodes of graph: ")
    print(graph.nodes())
    print("Edges of graph: ")
    print(graph.edges())
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos=pos, with_labels=True)
    plt.savefig("di_graph.png")
    plt.show()
