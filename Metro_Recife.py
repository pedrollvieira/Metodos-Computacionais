import heapq
import time
from collections import deque

# Função para encontrar o menor caminho usando o algoritmo de Dijkstra
def dijkstra_adj(graph, start):
    n = len(graph)
    distancias = [float('infinity')] * n
    predecessores = [-1] * n
    distancias[start] = 0
    pq = [(0, start)]
    visitados = set()

    while pq:
        dAtual, no_atual = heapq.heappop(pq)
        if no_atual in visitados:
            continue
        visitados.add(no_atual)
        for vizinho, tempo in graph[no_atual]:
            distancia = dAtual + tempo
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(pq, (distancia, vizinho))
    return distancias, predecessores

# Função para encontrar o menor caminho usando o algoritmo de Busca em Profundidade (DFS)
def dfs(graph, start):
    n = len(graph)
    distancias = [float('infinity')] * n
    predecessores = [-1] * n
    distancias[start] = 0
    stack = [(start, 0)]
    visitados = set()

    while stack:
        node, dAtual = stack.pop()
        if node in visitados:
            continue
        visitados.add(node)
        for vizinho, tempo in graph[node]:
            distancia = dAtual + tempo
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = node
                stack.append((vizinho, distancia))
    return distancias, predecessores

# Função para encontrar o menor caminho usando o algoritmo de Busca em Largura (BFS)
def bfs(graph, start):
    n = len(graph)
    distancias = [float('infinity')] * n
    predecessores = [-1] * n
    distancias[start] = 0
    queue = deque([start])
    visitados = set()

    while queue:
        node = queue.popleft()
        if node in visitados:
            continue
        visitados.add(node)
        for vizinho, tempo in graph[node]:
            if distancias[vizinho] == float('infinity'):
                distancias[vizinho] = distancias[node] + tempo
                predecessores[vizinho] = node
                queue.append(vizinho)
    return distancias, predecessores

# Função para reconstruir o caminho a partir dos predecessores
def reconstruir_caminho(predecessores, start, end):
    caminho = []
    atual = end
    while atual != -1:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()
    return caminho

# Função para calcular e imprimir o menor tempo de viagem usando Dijkstra, BFS e DFS
def calcular_menor_tempo(graph, no_inicial, no_final, estacoes):
    # Calcular menor tempo usando Dijkstra
    t0dij = time.time()
    menortempo, predecessores_dij = dijkstra_adj(graph, no_inicial)
    tfdij = time.time()
    tdij = tfdij - t0dij
    caminho_dij = reconstruir_caminho(predecessores_dij, no_inicial, no_final)
    print(f"Menor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por Dijkstra: {menortempo[no_final]} minutos")
    print(f"Caminho percorrido por Dijkstra: {' -> '.join(estacoes[i] for i in caminho_dij)}")
    print(f"Tempo de execução por Dijkstra: {tdij:.8f} segundos")

    # Calcular menor tempo usando BFS
    t0bfs = time.time()
    menortempo_bfs, predecessores_bfs = bfs(graph, no_inicial)
    tfbfs = time.time()
    tbfs = tfbfs - t0bfs
    caminho_bfs = reconstruir_caminho(predecessores_bfs, no_inicial, no_final)
    print(f"\nMenor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por BFS: {menortempo_bfs[no_final]} minutos")
    print(f"Caminho percorrido por BFS: {' -> '.join(estacoes[i] for i in caminho_bfs)}")
    print(f"Tempo de execução por BFS: {tbfs:.8f} segundos")

    # Calcular menor tempo usando DFS
    t0dfs = time.time()
    menortempo_dfs, predecessores_dfs = dfs(graph, no_inicial)
    tfdfs = time.time()
    tdfs = tfdfs - t0dfs
    caminho_dfs = reconstruir_caminho(predecessores_dfs, no_inicial, no_final)
    print(f"\nMenor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por DFS: {menortempo_dfs[no_final]} minutos")
    print(f"Caminho percorrido por DFS: {' -> '.join(estacoes[i] for i in caminho_dfs)}")
    print(f"Tempo de execução por DFS: {tdfs:.8f} segundos")

    # Comparar os tempos de execução dos algoritmos
    tempos_exec = {"Dijkstra": tdij, "BFS": tbfs, "DFS": tdfs}
    algoritmo_mais_rapido = min(tempos_exec, key=tempos_exec.get)
    tempoMenor = tempos_exec[algoritmo_mais_rapido]
    print(f"\nO algoritmo mais rápido foi: {algoritmo_mais_rapido} com {tempoMenor:.8f} segundos")

# Função para calcular e imprimir o menor tempo de viagem em um grafo não ponderado
def calcular_menor_tempo_nao_ponderado(graph_np, no_inicial, no_final, estacoes):
    # Calcular menor tempo usando Dijkstra
    t0dijNP = time.time()
    melhorTempoDijkstraNP, predecessores_dijNP = dijkstra_adj(graph_np, no_inicial)
    tfdijNP = time.time()
    tdijNP = tfdijNP - t0dijNP
    caminho_dijNP = reconstruir_caminho(predecessores_dijNP, no_inicial, no_final)

    # Calcular menor tempo usando BFS
    t0bfsNP = time.time()
    melhorTempobfsNP, predecessores_bfsNP = bfs(graph_np, no_inicial)
    tfbfsNP = time.time()
    tbfsNP = tfbfsNP - t0bfsNP
    caminho_bfsNP = reconstruir_caminho(predecessores_bfsNP, no_inicial, no_final)

    # Calcular menor tempo usando DFS
    t0dfsNP = time.time()
    melhorTempodfsNP, predecessores_dfsNP = dfs(graph_np, no_inicial)
    tfdfsNP = time.time()
    tdfsNP = tfdfsNP - t0dfsNP
    caminho_dfsNP = reconstruir_caminho(predecessores_dfsNP, no_inicial, no_final)

    # Comparar os tempos de execução dos algoritmos
    tempos_execNP = {"Dijkstra": tdijNP, "BFS": tbfsNP, "DFS": tdfsNP}
    algoritmo_mais_rapidoNP = min(tempos_execNP, key=tempos_execNP.get)
    tempoMenorNP = tempos_execNP[algoritmo_mais_rapidoNP]
    print(f"\nO algoritmo mais rápido com o grafo não-ponderado foi: {algoritmo_mais_rapidoNP} com {tempoMenorNP:.8f} segundos")

# Função para calcular e imprimir o menor tempo de viagem com uma nova conexão adicionada ao grafo
def calcular_menor_tempo_com_nova_conexao(graph_melhorado, no_inicial, no_final, estacoes):
    melhorTempoModificado, predecessores_modificado = dijkstra_adj(graph_melhorado, no_inicial)
    caminho_modificado = reconstruir_caminho(predecessores_modificado, no_inicial, no_final)
    print(f"\nMenor tempo de viagem de '{estacoes[no_inicial]}' para '{estacoes[no_final]}' por Dijkstra com a nova conexão foi de: {melhorTempoModificado[no_final]} minutos")
    print(f"Caminho percorrido por Dijkstra com a nova conexão: {' -> '.join(estacoes[i] for i in caminho_modificado)}")

def main():
    # Grafo representado como uma lista de adjacência
    graph_adj = [
        [(1, 4)], [(0, 4), (2, 3)], [(1, 3), (3, 5)], [(2, 5), (4, 3)], [(3, 3), (6, 2)],
        [(6, 2), (7, 3)], [(4, 2), (5, 2), (27, 4)], [(5, 3), (8, 2)], [(7, 2), (9, 3)],
        [(8, 3), (10, 4)], [(9, 4), (11, 2)], [(10, 2), (14, 5)], [(13, 2)], [(12, 2), (14, 4), (16, 5)],
        [(13, 4), (11, 5)], [(16, 5), (24, 10)], [(15, 5), (17, 6)], [(21, 6), (22, 6)], [(20, 4), (19, 7)],
        [(18, 7)], [(18, 4), (21, 4)], [(20, 4), (17, 6)], [(17, 6), (23, 3)], [(22, 3), (24, 3)],
        [(23, 3), (15, 10)], [(26, 5), (28, 5)], [(27, 12), (25, 5)], [(6, 4), (26, 12)], [(25, 5)]
    ]

    # Mapeamento de índices para estações
    estacoes = [
        'Camaragibe', 'Cosme e Damião', 'Rodoviária', 'Curado', 'Alto do Céu', 'Teijipió',
        'Coqueiral', 'Barro', 'Werneck', 'Santa Luzia', 'Mangueira', 'Ipiranga', 'Recife',
        'Joana Bezerra', 'Afogados', 'Imbiribeira', 'Largo da Paz', 'Aeroporto', 'Prazeres',
        'Cajueiro Seco', 'Monte dos Guararapes', 'Ponta Larga', 'Tancredo Neves', 'Shopping',
        'Antônio Falcão', 'Engenho Velho', 'Floriano', 'Cavaleiro', 'Jaboatão'
    ]

    # Definir o nó inicial e final
    no_inicial = 0
    no_final = 19

    # Calcular e imprimir o menor tempo de viagem usando Dijkstra, BFS e DFS
    calcular_menor_tempo(graph_adj, no_inicial, no_final, estacoes)

    # Definir um grafo não ponderado e repetir os cálculos
    graph_np = [
        [(1, 1)], [(0, 1), (2, 1)], [(1, 1), (3, 1)], [(2, 1), (4, 1)], [(3, 1), (6, 1)],
        [(6, 1), (7, 1)], [(4, 1), (5, 1), (27, 1)], [(5, 1), (8, 1)], [(7, 1), (9, 1)],
        [(8, 1), (10, 1)], [(9, 1), (11, 1)], [(10, 1), (14, 1)], [(13, 1)], [(12, 1), (14, 1), (16, 1)],
        [(13, 1), (11, 1)], [(16, 1), (24, 1)], [(15, 1), (17, 1)], [(21, 1), (22, 1)], [(20, 1), (19, 1)],
        [(18, 1)], [(18, 1), (21, 1)], [(20, 1), (17, 1)], [(17, 1), (23, 1)], [(22, 1), (24, 1)],
        [(23, 1), (15, 1)], [(26, 1), (28, 1)], [(27, 1), (25, 1)], [(6, 1), (26, 1)], [(25, 1)]
    ]

    calcular_menor_tempo_nao_ponderado(graph_np, no_inicial, no_final, estacoes)

    # Adicionar uma nova conexão ao grafo e calcular o menor tempo de viagem com a nova conexão
    graph_melhorado = [
        [(1, 4)], [(0, 4), (2, 3)], [(1, 3), (3, 5)], [(2, 5), (4, 3)], [(3, 3), (6, 2), (22, 20)],
        [(6, 2), (7, 3)], [(4, 2), (5, 2), (27, 4)], [(5, 3), (8, 2)], [(7, 2), (9, 3)], [(8, 3), (10, 4)],
        [(9, 4), (11, 2)], [(10, 2), (14, 5)], [(13, 2)], [(12, 2), (14, 4), (16, 5)], [(13, 4), (11, 5)],
        [(16, 5), (24, 10)], [(15, 5), (17, 6)], [(21, 6), (22, 6)], [(20, 4), (19, 7)], [(18, 7)],
        [(18, 4), (21, 4)], [(20, 4), (17, 6)], [(17, 6), (23, 3), (4, 20)], [(22, 3), (24, 3)],
        [(23, 3), (15, 10)], [(26, 5), (28, 5)], [(27, 12), (25, 5)], [(6, 4), (26, 12)], [(25, 5)]
    ]

    calcular_menor_tempo_com_nova_conexao(graph_melhorado, no_inicial, no_final, estacoes)

if __name__ == "__main__":
    main()