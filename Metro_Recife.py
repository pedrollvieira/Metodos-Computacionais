import heapq
import time
from collections import deque

# Função Dijkstra
def dijkstra_adj(graph, start):
    n = len(graph)
    distancias = [float('infinity')] * n
    distancias[start] = 0
    pq = [(0, start)]

    while pq:
        dAtual, no_atual = heapq.heappop(pq)
        if dAtual > distancias[no_atual]:
            continue
        for vizinho, tempo in graph[no_atual]:
            distancia = dAtual + tempo
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(pq, (distancia, vizinho))
    return distancias

# Função BFS
def bfs(graph, inicio):
    n = len(graph)
    distancias = [float('infinity')] * n
    distancias[inicio] = 0
    fila = deque([inicio])

    while fila:
        node = fila.popleft()
        for vizinho, tempo in graph[node]:
            if distancias[vizinho] == float('infinity'):
                distancias[vizinho] = distancias[node] + tempo
                fila.append(vizinho)
    return distancias

# Função DFS
def dfs(graph, inicio):
    n = len(graph)
    distancias = [float('infinity')] * n
    distancias[inicio] = 0
    stack = [(inicio, 0)]

    while stack:
        no, dAtual = stack.pop()
        for vizinho, tempo in graph[no]:
            distancia = dAtual + tempo
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                stack.append((vizinho, distancia))
    return distancias

# Grafo de adjacência
graph_adj = [
    [(1, 4)],  # Camaragibe
    [(0, 4), (2, 3)],  # Cosme e Damião
    [(1, 3), (3, 5)],  # Rodoviária
    [(2, 5), (4, 3)],  # Curado
    [(3, 3), (5, 6)],  # Alto do Céu
    [(4, 6), (6, 2)],  # Teijipió
    [(5, 2), (7, 3)],  # Coqueiral
    [(6, 3), (8, 2), (12, 10)],  # Barro
    [(7, 2), (9, 3)],  # Werneck
    [(8, 3), (10, 4)],  # Santa Luzia
    [(9, 4), (11, 2)],  # Mangueira
    [(10, 2), (14, 5)],  # Ipiranga
    [(7, 10), (13, 2)],  # Recife
    [(12, 2), (14, 4)],  # Joana Bezerra
    [(13, 4), (15, 5), (11, 5)],  # Afogados
    [(14, 5), (16, 3)],  # Imbiribeira
    [(15, 3), (17, 6)],  # Largo da Paz
    [(16, 6), (18, 7)],  # Aeroporto
    [(17, 5), (19, 7)],  # Prazeres
    [(18, 7)],  # Cajueiro Seco
]

# Lista de estações
estacoes = [
    'Camaragibe', 'Cosme e Damião', 'Rodoviária', 'Curado', 'Alto do Céu', 'Teijipió',
    'Coqueiral', 'Barro', 'Werneck', 'Santa Luzia', 'Mangueira', 'Ipiranga', 'Recife',
    'Joana Bezerra', 'Afogados', 'Imbiribeira', 'Largo da Paz', 'Aeroporto', 'Prazeres',
    'Cajueiro Seco'
]

no_inicial = 0
no_final = 19

# Calcular menor tempo usando Dijkstra
tempo_inicio = time.time()
menortempo_dijkstra = dijkstra_adj(graph_adj, no_inicial)
tempo_dijkstra = time.time() - tempo_inicio

# Calcular menor tempo usando BFS
tempo_inicio = time.time()
menortempo_bfs = bfs(graph_adj, no_inicial)
tempo_bfs = time.time() - tempo_inicio

# Calcular menor tempo usando DFS
tempo_inicio = time.time()
menortempo_dfs = dfs(graph_adj, no_inicial)
tempo_dfs = time.time() - tempo_inicio

menor_tempo = min(menortempo_dijkstra[no_final], menortempo_bfs[no_final], menortempo_dfs[no_final])

if menor_tempo == menortempo_dijkstra[no_final]:
    algoritmo_eficiente = "Dijkstra"
    tempo_execucao = tempo_dijkstra
elif menor_tempo == menortempo_bfs[no_final]:
    algoritmo_eficiente = "BFS"
    tempo_execucao = tempo_bfs
else:
    algoritmo_eficiente = "DFS"
    tempo_execucao = tempo_dfs

print(f"O algoritmo mais eficiente é {algoritmo_eficiente} com tempo de viagem de {menor_tempo} minutos")
#print('Tempo de execução: ', "--- %.10f segundos ---" % tempo_execucao)

# Proposta de nova conexão entre Alto do Céu (4) e Aeroporto (17) 
print("\nCom uma proposta de nova conexão entre Alto do Céu e Aeroporto, obtemos:")
no_inicial = 4
no_final = 17

menortempo_dijkstra = dijkstra_adj(graph_adj, no_inicial)
tempo_estimado = menortempo_dijkstra[no_final]

graph_adj[4].append((17, tempo_estimado))
graph_adj[17].append((4, tempo_estimado))

# Recalcular menor tempo usando o algoritmo mais eficiente
if algoritmo_eficiente == "Dijkstra":
    tempo_inicio = time.time()
    menortempo_dijkstra = dijkstra_adj(graph_adj, no_inicial)
    tempo_execucao = time.time() - tempo_inicio
    menor_tempo = menortempo_dijkstra[no_final]
elif algoritmo_eficiente == "BFS":
    tempo_inicio = time.time()
    menortempo_bfs = bfs(graph_adj, no_inicial)
    tempo_execucao = time.time() - tempo_inicio
    menor_tempo = menortempo_bfs[no_final]
else:
    tempo_inicio = time.time()
    menortempo_dfs = dfs(graph_adj, no_inicial)
    tempo_execucao = time.time() - tempo_inicio
    menor_tempo = menortempo_dfs[no_final]

print(f"Algoritmo mais eficiente é {algoritmo_eficiente} com tempo de viagem de {menor_tempo} minutos")
#print('Tempo de execução: ', "--- %.10f segundos ---" % tempo_execucao)