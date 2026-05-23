    
import heapq


def prim_algorithm(vertices, edges):
   
    n = len(vertices)
    t_mst = set()              
    d = {v: float('inf') for v in vertices} 
    parent = {v: None for v in vertices}   
    
    start_node = vertices[0]
    d[start_node] = 0
    parent[start_node] = start_node
    
   
    queue = [(0, start_node)]
    visited = set()

    while queue:
      
        current_dist, u = heapq.heappop(queue)
        
        if u in visited:
            continue
        visited.add(u)

    
        if parent[u] != u:
            t_mst.add((parent[u], u))

     
        for w, weight in edges.get(u, []):
            if w not in visited:
                if weight < d[w]:
                    d[w] = weight
                    parent[w] = u
                    heapq.heappush(queue, (d[w], w))
                elif parent[w] is None:
                    d[w] = weight
                    parent[w] = u
                    heapq.heappush(queue, (d[w], w))

    return t_mst
grafo = {
        0: [(1, 10), (2, 20)],
        1: [(0, 10), (3, 50), (4, 10)],
        2: [(0, 20), (3, 20), (4, 33)],
        3: [(1, 50), (2, 20), (4, 20), (5, 2)],
        4: [(1, 10), (2, 33), (3, 20), (5, 1)],
        5: [(3, 2), (4, 1)]
    }

resultado = prim_algorithm(grafo.keys(), grafo)
print("Aristas del MST:", resultado)