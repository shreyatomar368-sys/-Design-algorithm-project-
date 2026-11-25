
from algorithms.graph import create_graph
from algorithms.topological_sort import topological_sort_bfs
from algorithms.dfs_sort import topological_sort_dfs
from algorithms.cycle_detection import detect_cycle
from algorithms.graph_visualization import visualize_graph

# Sample project tasks
tasks = [
    "Requirement Analysis",
    "System Design",
    "Frontend Development",
    "Backend Development",
    "Database Design",
    "Integration",
    "Testing",
    "Deployment"
]

# Dependencies: prerequisite -> dependent task
dependencies = [
    ("Requirement Analysis", "System Design"),
    ("System Design", "Frontend Development"),
    ("System Design", "Backend Development"),
    ("System Design", "Database Design"),
    ("Frontend Development", "Integration"),
    ("Backend Development", "Integration"),
    ("Database Design", "Integration"),
    ("Integration", "Testing"),
    ("Testing", "Deployment")
]

# Create dependency graph
graph = create_graph(tasks, dependencies)

print("\n========== FLOWPILOT ==========")
print("\nDEPENDENCY GRAPH:")
for task, neighbours in graph.items():
    print(f"{task} -> {neighbours}")

print("\nBFS / KAHN'S ALGORITHM:")
print("Execution Order:", topological_sort_bfs(graph))

print("\nDFS TOPOLOGICAL SORT:")
print("Execution Order:", topological_sort_dfs(graph))

print("\nCYCLE DETECTION:")
if detect_cycle(graph):
    print("Cycle detected! No valid execution order.")
else:
    print("No cycle detected. Project execution is possible.")



print("\n========== CYCLE TEST ==========")

cyclic_graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

if detect_cycle(cyclic_graph):
    print("Cycle detected! Invalid dependency graph.")
else:
    print("No cycle detected.")

try:
    topological_sort_bfs(cyclic_graph)
except ValueError as error:
    print("BFS:", error)

try:
    topological_sort_dfs(cyclic_graph)
except ValueError as error:
    print("DFS:", error)



print("\nGenerating Dependency Graph...")
visualize_graph(graph)