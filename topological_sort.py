
from collections import deque


def topological_sort_bfs(graph):
    # Calculate indegree of every task
    indegree = {task: 0 for task in graph}

    for task in graph:
        for neighbour in graph[task]:
            indegree[neighbour] += 1

    # Add tasks with zero indegree to the queue
    queue = deque()

    for task in indegree:
        if indegree[task] == 0:
            queue.append(task)

    result = []

    # Process tasks using BFS
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbour in graph[current]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # Check for cycles
    if len(result) != len(graph):
        raise ValueError("Cycle detected! No valid execution order.")

    return result
