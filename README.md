# DFS Algorithm (Recursive)

DFS(graph, start, visited):
     Add start to visited
     Print or process start

     For each neighbor in graph[start]:
         If neighbor not in visited:
             Call DFS(graph, neighbor, visited)
             
**Algorithm BFS(graph, start)**

 visited ← [start]
 queue ← [start]

 while queue is not empty do
      a. node ← remove first element from queue
      b. print node
      c. for each neighbor in graph[node] do
            if neighbor not in visited then
                 add neighbor to visited
                 add neighbor to queue
 end while

 **Algorithm: Uniform Cost Search (UCS)**

 Initialize queue ← [(0, start)]

 While queue is not empty:
     a. Sort queue by cost
     b. Remove (cost, node) with lowest cost
     c. If node == goal:
           Print cost and stop
     d. For each (neighbor, weight) in graph[node]:
           Add (cost + weight, neighbor) to queue



 
