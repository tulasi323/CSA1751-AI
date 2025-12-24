def ucs(graph, start, goal):
    queue = [(0, start)]

    while queue:
        queue.sort()
        cost, node = queue.pop(0)

        if node == goal:
            print(cost)
            return

        for n, w in graph[node]:
            queue.append((cost + w, n))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

ucs(graph, 'A', 'D')
