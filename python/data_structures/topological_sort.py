
graph = {
    0: [2, 3],
    1: [],
    2: [3],
    3: [5],
    4: [],
    5: [],
    6: [7],
    7: []
}


def topological_sort_util(node, visited, stack):
    visited.add(node)
    
    for child in graph[node]:
        if child not in visited:
            topological_sort_util(child, visited, stack)

    stack.append(node)


def topological_sort(graph):
    stack = []
    visited = set()

    for node in graph.keys():
        if node not in visited:
            topological_sort_util(node, visited, stack)

    return stack[::-1]


if __name__ == '__main__':
    print(topological_sort(graph))




