def astar(graph, h, start, goal):
    q = [(h[start], 0, start)]  # (f, g, node)

    while q:
        q.sort()
        f, g, n = q.pop(0)

        if n == goal:
            print(g)
            return

        for x, w in graph[n]:
            q.append((g + w + h[x], g + w, x))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A':3, 'B':1, 'C':1, 'D':0}

astar(graph, h, 'A', 'D')
