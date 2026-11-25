
import random
import time
import matplotlib.pyplot as plt
import pandas as pd

from algorithms.topological_sort import topological_sort_bfs
from algorithms.dfs_sort import topological_sort_dfs


# Generate a random Directed Acyclic Graph (DAG)
def generate_graph(vertices, probability=0.02):
    graph = {i: [] for i in range(vertices)}

    for i in range(vertices):
        for j in range(i + 1, vertices):
            if random.random() < probability:
                graph[i].append(j)

    return graph


# Measure average execution time
def measure_time(algorithm, graph, runs=10):
    execution_times = []

    for _ in range(runs):
        start = time.perf_counter()
        algorithm(graph)
        end = time.perf_counter()

        execution_times.append(end - start)

    return sum(execution_times) / runs


def run_benchmark():
    random.seed(42)

    graph_sizes = [50, 100, 200, 400, 800]

    bfs_times = []
    dfs_times = []
    edge_counts = []

    print("\n========== FLOWPILOT PERFORMANCE ANALYSIS ==========")

    for size in graph_sizes:
        graph = generate_graph(size)

        edges = sum(len(neighbours) for neighbours in graph.values())

        bfs_avg = measure_time(topological_sort_bfs, graph)
        dfs_avg = measure_time(topological_sort_dfs, graph)

        bfs_times.append(bfs_avg)
        dfs_times.append(dfs_avg)
        edge_counts.append(edges)

        print(f"\nTasks: {size}")
        print(f"Dependencies: {edges}")
        print(f"BFS Average Time: {bfs_avg:.8f} seconds")
        print(f"DFS Average Time: {dfs_avg:.8f} seconds")

    # Create results table
    results = pd.DataFrame({
        "Tasks": graph_sizes,
        "Dependencies": edge_counts,
        "BFS Time (seconds)": bfs_times,
        "DFS Time (seconds)": dfs_times
    })

    print("\n========== PERFORMANCE TABLE ==========")
    print(results.to_string(index=False))

    # Draw performance comparison chart
    plt.figure(figsize=(10, 6))

    plt.plot(
        graph_sizes,
        bfs_times,
        marker="o",
        label="BFS / Kahn's Algorithm"
    )

    plt.plot(
        graph_sizes,
        dfs_times,
        marker="s",
        label="DFS Algorithm"
    )

    plt.xlabel("Number of Tasks (Vertices)")
    plt.ylabel("Average Execution Time (Seconds)")
    plt.title("FlowPilot - BFS vs DFS Performance Comparison")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        "results/performance_comparison.png",
        dpi=300
    )

    plt.show()

    # Save benchmark data
    results.to_csv("results/performance_results.csv", index=False)

    print("\nPerformance chart saved successfully!")
    print("Performance data saved successfully!")


if __name__ == "__main__":
    run_benchmark()
