import heapq

def dijkstra_con_caminos(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[inicio] = 0
    
    pq = [(0, inicio)]
    
    while pq:
        distancia_actual, u = heapq.heappop(pq)
        
        if distancia_actual > distancias[u]:
            continue
            
        for v, peso in grafo[u]:
            distancia_nueva = distancia_actual + peso
            
            if distancia_nueva < distancias[v]:
                distancias[v] = distancia_nueva
                predecesores[v] = u  
                heapq.heappush(pq, (distancia_nueva, v))
                
    return distancias, predecesores

def obtener_camino(predecesores, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual) 
        actual = predecesores[actual]
    return camino

grafo = {
    0: [(1, 9), (4, 6)],
    1: [(0, 9), (3, 8)],
    2: [(4, 5), (5, 6)],
    3: [(1, 8), (5, 1), (7, 7)],
    4: [(0, 6), (2, 5), (6, 3)],
    5: [(2, 6), (3, 1)],
    6: [(4, 3), (7, 2)],
    7: [(3, 7), (6, 2)]
}

inicio = 0
distancias, padres = dijkstra_con_caminos(grafo, inicio)

print(f"Caminos más cortos desde el nodo {inicio}:")
print("-" * 40)

for nodo in grafo:
    camino = obtener_camino(padres, nodo)
    if distancias[nodo] == float('inf'):
        print(f"Nodo {nodo}: No es alcanzable")
    else:
      
        print(f"Nodo {nodo} (Distancia {distancias[nodo]}): {' -> '.join(map(str, camino))}")