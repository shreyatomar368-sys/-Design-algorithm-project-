
def create_graph(tasks, dependencies):
    graph = {task: [] for task in tasks}

    for source, destination in dependencies:
        if source not in graph or destination not in graph:
            raise ValueError("Dependency contains an unknown task.")

        graph[source].append(destination)

    return graph
