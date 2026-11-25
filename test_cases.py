
from algorithms.topological_sort import topological_sort_bfs
from algorithms.dfs_sort import topological_sort_dfs
from algorithms.cycle_detection import detect_cycle


def test_graph(name, graph):
    print(f"\n========== {name} ==========")

    if detect_cycle(graph):
        print("Cycle detected!")
        return

    bfs_order = topological_sort_bfs(graph)
    dfs_order = topological_sort_dfs(graph)

    print("BFS Order:", bfs_order)
    print("DFS Order:", dfs_order)
    print("Cycle Detection: No cycle detected")


# Test 1: Empty graph
test_graph("EMPTY GRAPH", {})

# Test 2: Single task
test_graph("SINGLE TASK", {
    "Planning": []
})

# Test 3: Independent tasks
test_graph("INDEPENDENT TASKS", {
    "Frontend": [],
    "Backend": [],
    "Database": []
})

# Test 4: Branching dependencies
test_graph("BRANCHING GRAPH", {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
})

# Test 5: Cyclic dependencies
test_graph("CYCLIC GRAPH", {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
})
