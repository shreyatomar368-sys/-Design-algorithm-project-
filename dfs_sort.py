
def topological_sort_dfs(graph):
    visited = set()
    recursion_stack = set()
    result = []

    def dfs(task):
        if task in recursion_stack:
            raise ValueError("Cycle detected! No valid execution order.")

        if task in visited:
            return

        visited.add(task)
        recursion_stack.add(task)

        for neighbour in graph[task]:
            dfs(neighbour)

        recursion_stack.remove(task)
        result.append(task)

    for task in graph:
        if task not in visited:
            dfs(task)

    return result[::-1]
