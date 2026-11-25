
def detect_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(task):
        visited.add(task)
        recursion_stack.add(task)

        for neighbour in graph[task]:

            if neighbour not in visited:
                if dfs(neighbour):
                    return True

            elif neighbour in recursion_stack:
                return True

        recursion_stack.remove(task)
        return False

    for task in graph:
        if task not in visited:
            if dfs(task):
                return True

    return False
