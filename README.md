
# FlowPilot
## Smart Dependency and Project Execution Manager

### 1. Introduction
FlowPilot is a graph-based project execution manager.
It represents project tasks as vertices and dependencies
as directed edges.

### 2. Objectives
- Represent project tasks using graphs.
- Identify task dependencies.
- Implement BFS/Kahn's topological sorting.
- Implement DFS topological sorting.
- Detect cycles in dependency graphs.
- Compare algorithm performance.
- Visualize project dependencies.

### 3. Algorithms Used
1. BFS - Kahn's Algorithm
2. DFS - Topological Sorting
3. DFS-based Cycle Detection

### 4. Time Complexity
BFS/Kahn's Algorithm: O(V + E)
DFS Topological Sorting: O(V + E)
Cycle Detection: O(V + E)

V = Number of vertices (tasks)
E = Number of edges (dependencies)

### 5. Technologies Used
- Python
- NetworkX
- Matplotlib
- Pandas

### 6. Results
The project successfully generates:
- Valid task execution orders.
- Cycle detection results.
- Dependency graph visualization.
- BFS vs DFS performance comparison.
- Performance results in CSV format.

### 7. Conclusion
FlowPilot demonstrates how graph algorithms can
solve real-world project scheduling problems.
Topological sorting ensures that prerequisite
tasks are completed before dependent tasks.
