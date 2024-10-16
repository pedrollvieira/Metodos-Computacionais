import heapq
import time
from collections import deque

# Função Dijkstra
def dijkstra_adj(graph, start):
    n = len(graph)
    distancias = [float('infinity')] * n   # inicialmente todas as distâncias são infinitas
    distancias[start] = 0                  # distância do nó para ele mesmo (início) é nula
    pq = [(0, start)]                      # fila de prioridade que é inicializada com o primeiro nó

    while pq:                              # o loop continua enquanto a lista de prioridade não estiver vazia
        dAtual, no_atual = heapq.heappop(pq) # remove e retorna o nó com menor distância da lista de prioridade
        if dAtual > distancias[no_atual]:
            continue
        for vizinho, tempo in graph[no_atual]:
            distancia = dAtual + tempo
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(pq, (distancia, vizinho)) # adiciona o nó vizinho à lista de prioridades
    return distancias

# Função BFS
def bfs(graph, inicio):
    n = len(graph)
    distancias = [float('infinity')] * n # definindo as distâncias para os outros nós como infinito
    distancias[inicio] = 0               # distância do nó para ele mesmo sendo 0
    fila = deque([inicio])               # inserindo o nó inicial em uma fila

    while fila:                          # enquanto a fila tiver algum elemento
        node = fila.popleft()            # remove o primeiro nó da fila
        for vizinho, tempo in graph[node]:
            if distancias[vizinho] == float('infinity'): # se o nó ainda não tiver sido visitado, a distância vai ser infinita
                distancias[vizinho] = distancias[node] + tempo # atualiza a distância do vizinho
                fila.append(vizinho)    # adiciona o vizinho à fila e continua o loop até todos os nós serem descobertos
    return distancias

# Função DFS
def dfs(graph, inicio):
    n = len(graph)
    distancias = [float('infinity')] * n
    distancias[inicio] = 0
    stack = [(inicio, 0)] # aqui cria uma pilha com o nó inicial

    while stack:                 # enquanto a pilha tiver algum nó
        no, dAtual = stack.pop() # remove o último nó da pilha
        for vizinho, tempo in graph[no]: # pra cada vizinho e tempo, vai atualizar a distância com a do próximo vizinho
            distancia = dAtual + tempo
            if distancia < distancias[vizinho]: # se a próxima distância for menor do que a registrada, atualiza a distância e adiciona o vizinho à pilha
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
print(f"Menor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por Dijkstra: {menortempo_dijkstra[no_final]} minutos")
print('tempo de execução: ', "--- %.7f segundos ---" % (time.time() - tempo_inicio))

# Calcular menor tempo usando BFS
tempo_inicio = time.time()
menortempo_bfs = bfs(graph_adj, no_inicial)
print(f"Menor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por BFS: {menortempo_bfs[no_final]} minutos")
print('tempo de execução: ', "--- %.7f segundos ---" % (time.time() - tempo_inicio))

# Calcular menor tempo usando DFS
tempo_inicio = time.time()
menortempo_dfs = dfs(graph_adj, no_inicial)
print(f"Menor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por DFS: {menortempo_dfs[no_final]} minutos")
print('tempo de execução: ', "--- %.7f segundos ---" % (time.time() - tempo_inicio))