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

 
