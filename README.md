# DFS Algorithm (Recursive)

DFS(graph, start, visited):
     Add start to visited
     Print or process start

     For each neighbor in graph[start]:
         If neighbor not in visited:
             Call DFS(graph, neighbor, visited)
