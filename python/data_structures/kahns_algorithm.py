from collections import deque

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


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.in_degree = 0
        self.neighbors = neighbors
        self.count = 0


def kahns_algorithm(graph):
    nodes = {node: Node(node, neighbors) for node, neighbors in graph.items()}
    for neighbors in graph.values():
        for neighbor in neighbors:
            nodes[neighbor].in_degree += 1

    q = deque([node for node in nodes.values() if node.in_degree == 0])

    topologic_sort = []

    while q:
        node = q.popleft()
        node.count += 1

        topologic_sort.append(node.val)

        for neighbor in node.neighbors:
            nodes[neighbor].in_degree -= 1
            if nodes[neighbor].in_degree == 0:
                q.append(nodes[neighbor])

    if sum([node.count for node in nodes.values()]) != len(graph.keys()):
        print ("There was a cycle!")
    else:
        print(topologic_sort)
        return topologic_sort

    
if __name__ == '__main__':
    kahns_algorithm(graph)
