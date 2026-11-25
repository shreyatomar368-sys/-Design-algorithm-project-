
import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph):
    G = nx.DiGraph()

    # Add tasks and dependency edges
    for task, neighbours in graph.items():
        G.add_node(task)

        for neighbour in neighbours:
            G.add_edge(task, neighbour)

    # Arrange graph nodes
    position = nx.spring_layout(G, seed=42, k=1.5)

    plt.figure(figsize=(14, 9))

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        position,
        node_color="skyblue",
        node_size=3000,
        edgecolors="navy"
    )

    # Draw dependency arrows
    nx.draw_networkx_edges(
        G,
        position,
        edge_color="gray",
        arrows=True,
        arrowsize=25,
        width=2,
        connectionstyle="arc3,rad=0.08"
    )

    # Draw task names
    nx.draw_networkx_labels(
        G,
        position,
        font_size=8,
        font_weight="bold"
    )

    plt.title(
        "FlowPilot - Project Dependency Graph",
        fontsize=16,
        fontweight="bold"
    )

    plt.axis("off")
    plt.tight_layout()

    # Save graph image
    plt.savefig(
        "results/dependency_graph.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
