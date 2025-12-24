def gbfs(g, h, s, d):
    q = [(h[s], s)]
    v = set()

    while q:
        q.sort()
        _, n = q.pop(0)
        print(n, end=" ")

        if n == d:
            return

        v.add(n)
        for x in g[n]:
            if x not in v:
                q.append((h[x], x))

g = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

h = {'A':3, 'B':1, 'C':1, 'D':0}

gbfs(g, h, 'A', 'D')
