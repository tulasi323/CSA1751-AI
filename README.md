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
           
****Algorithm: A* Search (Best Algorithm)****
 q ← [(h[start], 0, start)]
   
  While q is not empty:
     a. Sort q by f = g + h
     b. Remove node with lowest f
     c. If node == goal:
           Print path cost and stop
     d. For each neighbor:
           Add (new f, new g, neighbor) to q

**Algorithm: Greedy Best-First Search (GBFS)**

Function GBFS(graph, h, start, goal):

1. q ← [(h[start], start)]
2. visited ← empty set

3. While q is not empty:
     a. Sort q by heuristic value
     b. Remove (h, node) with lowest value
     c. Print node
     d. If node == goal:
           Stop
     e. Add node to visited
     f. For each neighbor of node:
           If neighbor not in visited:
                Add (h[neighbor], neighbor) to q


**Algorithm: Minimax**

Function Minimax(depth, node, isMax, values):

1. If depth == 0:
      Return values[node]

2. If isMax == True:
      Return maximum of:
          Minimax(depth −

 Algorithm: Minimax

Function Minimax(node, depth, maximizing):

1. If depth == 0 or node has no children:
     Return score[node]

2. If maximizing:
     Return max(Minimax(child, depth-1, False) for child in children[node])

3. Else:
     Return min(Minimax(child, depth-1, True) for child in children[node])




