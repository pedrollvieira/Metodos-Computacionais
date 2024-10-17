import time
from datetime import datetime
import copy

# Função para converter a data e hora do evento em um objeto datetime
def data_hora(evento):
    return datetime.strptime(evento['data'] + ' ' + evento['hora'], '%d/%m/%Y %H:%M')

# Função para comparar a data/hora de dois eventos
def comparar_data_hora(evento1, evento2):
    data_hora1 = data_hora(evento1)
    data_hora2 = data_hora(evento2)
    if data_hora1 < data_hora2:
        return -1
    elif data_hora1 > data_hora2:
        return 1
    else:
        return 0

# Função para ordenar a lista de eventos usando Mergesort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lado_esquerdo = lista[:meio]
    lado_direito = lista[meio:]

    lado_esquerdo = merge_sort(lado_esquerdo)
    lado_direito = merge_sort(lado_direito)

    return merge(lado_esquerdo, lado_direito)

# Função para mesclar as duas metades da lista e ordenar segundo a data/hora
def merge(lado_esquerdo, lado_direito):
    lista_ordenada = []
    i = j = 0

    while i < len(lado_esquerdo) and j < len(lado_direito):
        if comparar_data_hora(lado_esquerdo[i], lado_direito[j]) <= 0:
            lista_ordenada.append(lado_esquerdo[i])
            i += 1
        else:
            lista_ordenada.append(lado_direito[j])
            j += 1

    lista_ordenada.extend(lado_esquerdo[i:])
    lista_ordenada.extend(lado_direito[j:])
    return lista_ordenada

# Função para ordenar a lista de eventos usando Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[len(lista) // 2]
    
    def dividir_lista(lista, pivot):
        esquerda = [x for x in lista if comparar_data_hora(x, pivot) < 0]
        meio = [x for x in lista if comparar_data_hora(x, pivot) == 0]
        direita = [x for x in lista if comparar_data_hora(x, pivot) > 0]
        return esquerda, meio, direita

    esquerda, meio, direita = dividir_lista(lista, pivot)

    return quicksort(esquerda) + meio + quicksort(direita)

# Função para ordenar a lista de eventos usando Heapsort
def heap_sort(lista):
    def posicao(lista, indice):
        return lista[indice - 1]

    def troca(lista, indice1, indice2):
        if indice1 > len(lista) or indice2 > len(lista):
            return
        lista[indice1 - 1], lista[indice2 - 1] = lista[indice2 - 1], lista[indice1 - 1]

    def max_heapify(lista, tamanho, pai):
        esquerda = 2 * pai
        direita = 2 * pai + 1
        maior = pai

        if esquerda <= tamanho and comparar_data_hora(posicao(lista, esquerda), posicao(lista, pai)) > 0:
            maior = esquerda

        if direita <= tamanho and comparar_data_hora(posicao(lista, direita), posicao(lista, maior)) > 0:
            maior = direita

        if maior != pai:
            troca(lista, maior, pai)
            max_heapify(lista, tamanho, maior)

    def construir_heap(tamanho, lista):
        inicio = tamanho // 2
        for i in range(inicio, 0, -1):
            max_heapify(lista, tamanho, i)

    tamanho = len(lista)
    construir_heap(tamanho, lista)

    for i in range(tamanho, 1, -1):
        troca(lista, 1, i)
        tamanho -= 1
        max_heapify(lista, tamanho, 1)

    return lista

# Função para adicionar novos eventos à lista
def adicionar_evento(lista):
    ''' 
    nome = input('Digite o nome do evento: ')
    dia = input('Digite o dia do evento: ')
    hora = input('Digite a hora do evento: ')
    local = input('Digite o local do evento: ')
    evento = {'nome': nome, 'data': dia, 'hora': hora, 'local': local}
    lista.append(evento)
    return lista
    '''
    novos_eventos = [
        {'nome': 'Olha! Recife Noturno', 'data': '01/10/2024', 'hora': '21:00', 'local': 'Tour Histórico'},
        {'nome': 'Olha! Recife Pedalando', 'data': '29/09/2024', 'hora': '09:00', 'local': 'Antigos Cinemas do Recife'},
        {'nome': 'Olha! Recife Barco', 'data': '26/09/2024', 'hora': '12:00', 'local': 'Passeio no Capibaribe'},
    ]

    lista.extend(novos_eventos)
    return lista

# Função para remover eventos da lista
def remover_evento(lista):
    ''' 
    nome = input('Digite o nome do evento que deseja remover: ')
    dia = input('Digite o dia do evento que deseja remover: ')
    hora = input('Digite a hora do evento que deseja remover: ')
    local = input('Digite o local do evento que deseja remover: ')
    evento = {'nome': nome, 'data': dia, 'hora': hora, 'local': local}
    lista.remove(evento)
    return lista
    '''
    pass


# Função para alterar data/hora de um evento
def alterar_evento(lista):
    ''' 
    print('Evento antigo')
    nome_evento = input('Digite o nome do evento que deseja alterar: ')
    dia_evento = input('Digite o dia do evento (formato: dd/mm/aaaa): ')
    hora_evento = input('Digite a hora do evento (formato: hh:mm): ')
    local_evento = input('Digite o local do evento: ')

    print('\nEvento novo')
    novo_dia = input('Digite o novo dia do evento (formato: dd/mm/aaaa): ')
    nova_hora = input('Digite a nova hora do evento (formato: hh:mm): ')
    novo_local = input('Digite o novo local do evento: ')

    # Itera sobre a lista de eventos para encontrar o evento correspondente
    for evento in lista:
        # Verifica se o nome, dia, hora e local do evento correspondem ao evento antigo
        if (evento['nome'] == nome_evento and 
            evento['data'] == dia_evento and 
            evento['hora'] == hora_evento and 
            evento['local'] == local_evento):
            # Atualiza os detalhes do evento
            evento['data'] = novo_dia
            evento['hora'] = nova_hora
            evento['local'] = novo_local
            print('Evento alterado com sucesso!')
            break
    else:
        # Se o evento não for encontrado, informa ao usuário
        print('Evento não encontrado.')
    return lista
    '''
    pass

# Função para identificar o método de ordenação a ser utilizado
def metodo_ordenacao(lista, metodo=''):
    if metodo == 'mergesort':
        return merge_sort(lista)
    elif metodo == 'quicksort':
        return quicksort(lista)
    elif metodo == 'heapsort':
        return heap_sort(lista)

# Função para identificar se houve mudanças na lista inicial de eventos
def houve_mudanca(lista_inicial, lista_atual):
    if len(lista_inicial) != len(lista_atual):
        return True
    for evento_inicial, evento_atual in zip(lista_inicial, lista_atual):
        if evento_inicial != evento_atual:
            return True
    return False

# Função para comparar os tempos de execução e imprimir o melhor
def comparar_tempos(tempos):
    melhor_metodo = min(tempos, key=tempos.get)
    print(f'O melhor método é {melhor_metodo} com tempo de execução de {tempos[melhor_metodo]:.10f} segundos')

def menu():
    ''' 
    print('1 - Para adicionar um novo evento')
    print('2 - Para remover um evento existente')
    print('3 - Para alterar um evento existente')
    print('4 - Executar a ordenação dos eventos')
    print('5 - Sair')
    opcao = input('Digite a opção desejada: ')
    return opcao
    '''
    pass

def main():
    lista_inicial = [
        {'nome': 'Olha! Recife a Pé', 'data': '27/09/2024', 'hora': '09:30', 'local': 'Recife Walking Tour'},
        {'nome': 'Olha! Recife no Rio', 'data': '28/09/2024', 'hora': '09:00', 'local': 'Ilha de Deus'},
        {'nome': 'Olha! Recife de Ônibus', 'data': '28/09/2024', 'hora': '09:00', 'local': 'Jardim Botânico'},
        {'nome': 'Olha! Recife de Ônibus', 'data': '28/09/2024', 'hora': '14:00', 'local': 'Instituto Ricardo Brennand'},
        {'nome': 'Olha! Recife de Ônibus', 'data': '29/09/2024', 'hora': '13:00', 'local': 'Fundação Gilberto Freyre'},
        {'nome': 'Olha! Recife Pedalando', 'data': '29/09/2024', 'hora': '09:00', 'local': 'Antigos Cinemas do Recife'},
        {'nome': 'Olha! Recife a Pé', 'data': '02/10/2024', 'hora': '14:00', 'local': 'Pátio do Terço e Arredores'},
        {'nome': 'Olha! Recife a Pé', 'data': '04/10/2024', 'hora': '09:30', 'local': 'Recife Walking Tour'},
    ]
    
    # Ordenar a lista inicial com cada método
    lista_mergesort = metodo_ordenacao(copy.deepcopy(lista_inicial), 'mergesort')
    lista_quicksort = metodo_ordenacao(copy.deepcopy(lista_inicial), 'quicksort')
    lista_heapsort = metodo_ordenacao(copy.deepcopy(lista_inicial), 'heapsort')

    """ 
    obs: decide deixar toda essa parte de escolha do usuário comentada, pois foquei na proposta principal do projeto

    opcao = menu()
    while opcao != '5':
        if opcao == '1':
            lista_mergesort = adicionar_evento(lista_mergesort)
            lista_quicksort = adicionar_evento(lista_quicksort)
            lista_heapsort = adicionar_evento(lista_heapsort)
        elif opcao == '2':
            lista_mergesort = remover_evento(lista_mergesort)
            lista_quicksort = remover_evento(lista_quicksort)
            lista_heapsort = remover_evento(lista_heapsort)
        elif opcao == '3':
            lista_mergesort = alterar_evento(lista_mergesort)
            lista_quicksort = alterar_evento(lista_quicksort)
            lista_heapsort = alterar_evento(lista_heapsort)
        elif opcao == '4':
            break
        else:
            print('Opção inválida. Tente novamente.')
        opcao = menu()
    """

    # Adicionar novos eventos à lista ordenada
    lista_mergesort = adicionar_evento(lista_mergesort)
    lista_quicksort = adicionar_evento(lista_quicksort)
    lista_heapsort = adicionar_evento(lista_heapsort)

    # Dicionário para armazenar os tempos de execução
    tempos = {}

    # Identificar se houve mudanças na lista inicial e reordenar de acordo com cada método
    # Medindo o tempo de execução de cada método e armazenando em _tempos_
    if houve_mudanca(lista_inicial, lista_mergesort):
        start_time = time.time()
        lista_nova_merge = metodo_ordenacao(lista_mergesort, 'mergesort')
        tempos['mergesort'] = time.time() - start_time
    
    if houve_mudanca(lista_inicial, lista_quicksort):
        start_time = time.time()
        lista_nova_quick = metodo_ordenacao(lista_quicksort, 'quicksort')
        tempos['quicksort'] = time.time() - start_time

    if houve_mudanca(lista_inicial, lista_heapsort):
        start_time = time.time()
        lista_nova_heap = metodo_ordenacao(lista_heapsort, 'heapsort')
        tempos['heapsort'] = time.time() - start_time

    # Imprimir as listas ordenadas de acordo com cada método
    print("\nLista ordenada com Merge Sort:")
    for evento in lista_nova_merge:
        print(evento)

    print("\nLista ordenada com Quick Sort:")
    for evento in lista_nova_quick:
        print(evento)

    print("\nLista ordenada com Heap Sort:")
    for evento in lista_nova_heap:
        print(evento)

    # Imprimir os tempos de execução de cada método
    print("\n")
    print(f"Tempo de execução do Merge Sort: {tempos['mergesort']:.10f} segundos")
    print(f"Tempo de execução do Quick Sort: {tempos['quicksort']:.10f} segundos")
    print(f"Tempo de execução do Heap Sort: {tempos['heapsort']:.10f} segundos")

    # Comparar os tempos de execução e imprimir o melhor
    comparar_tempos(tempos)

if __name__ == "__main__":
    main()