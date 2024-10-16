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

    # Encontrando o meio da lista e dividindo-a em duas partes
    meio = len(lista) // 2
    lado_esquerdo = lista[:meio]
    lado_direito = lista[meio:]

    # Chamando a função recursivamente para dividir as partes restantes
    lado_esquerdo = merge_sort(lado_esquerdo)
    lado_direito = merge_sort(lado_direito)

    # Mesclando as duas partes ordenadas
    return merge(lado_esquerdo, lado_direito)

# Função para mesclar as duas metades da lista e ordenar segundo a data/hora
def merge(lado_esquerdo, lado_direito):
    # Lista para armazenar a lista_ordenada
    lista_ordenada = []
    i = j = 0

    # Comparando os elementos de cada lista
    while i < len(lado_esquerdo) and j < len(lado_direito):
        # Comparando as datas/horas dos eventos. Se a data/hora do lado esquerdo for menor, adicionar o evento a lista_ordenada
        if comparar_data_hora(lado_esquerdo[i], lado_direito[j]) <= 0:
            lista_ordenada.append(lado_esquerdo[i])
            i += 1
        # Caso contrário, adicionar o evento do lado direito ao lista_ordenada
        else:
            lista_ordenada.append(lado_direito[j])
            j += 1

    # Adicionando os elementos restantes de cada lista
    lista_ordenada.extend(lado_esquerdo[i:])
    lista_ordenada.extend(lado_direito[j:])
    return lista_ordenada

# Função para ordenar a lista de eventos usando Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    # Escolhendo o pivot como o elemento do meio da lista
    pivot = lista[len(lista) // 2]
    
    # Função para dividir a lista em três partes (esquerda, meio e direita) em relação ao pivot
    def dividir_lista(lista, pivot):
        '''
        esquerda: eventos com data/hora menor que o pivot
        meio: eventos com data/hora igual ao pivot
        direita: eventos com data/hora maior que o pivot
        '''
        esquerda = [x for x in lista if comparar_data_hora(x, pivot) < 0]
        meio = [x for x in lista if comparar_data_hora(x, pivot) == 0]
        direita = [x for x in lista if comparar_data_hora(x, pivot) > 0]
        return esquerda, meio, direita

    esquerda, meio, direita = dividir_lista(lista, pivot)

    # Chamando a função recursivamente para ordenar as partes esquerda e direita
    return quicksort(esquerda) + meio + quicksort(direita)

# Função para ordenar a lista de eventos usando Heapsort
def heap_sort(lista):
    # Função para acessar o elemento no índice ajustado
    def posicao(lista, indice):
        return lista[indice - 1]  # indexação ajustada para começar em 1

    # Função para trocar elementos na lista
    def troca(lista, indice1, indice2):
        if indice1 > len(lista) or indice2 > len(lista):
            return
        lista[indice1 - 1], lista[indice2 - 1] = lista[indice2 - 1], lista[indice1 - 1]

    # Função para garantir que a propriedade do heap máximo seja mantida
    def max_heapify(lista, tamanho, pai):
        esquerda = 2 * pai  # índice do filho esquerdo
        direita = 2 * pai + 1  # índice do filho direito
        maior = pai  # inicializa maior com índice do pai

        # Verificar se o filho esquerdo é maior que o pai
        if esquerda <= tamanho and comparar_data_hora(posicao(lista, esquerda), posicao(lista, pai)) > 0:
            maior = esquerda

        # Verificar se o filho direito é maior que o pai
        if direita <= tamanho and comparar_data_hora(posicao(lista, direita), posicao(lista, maior)) > 0:
            maior = direita

        # Se o maior elemento não é o pai, trocar as posições
        if maior != pai:
            troca(lista, maior, pai)
            max_heapify(lista, tamanho, maior)  # Garantir que a regra se repita na subárvore

    # Função para construir o heap máximo
    def construir_heap(tamanho, lista):
        inicio = tamanho // 2  # calcula o índice do último nó pai
        for i in range(inicio, 0, -1):
            max_heapify(lista, tamanho, i)

    # Construir o heap máximo
    tamanho = len(lista)
    construir_heap(tamanho, lista)

    # Extrair elementos do heap um por um
    for i in range(tamanho, 1, -1):
        troca(lista, 1, i)
        tamanho -= 1
        max_heapify(lista, tamanho, 1)  # Chamar max_heapify na raiz para ajustar o heap

    return lista

# Função para adicionar novos eventos à lista
def adicionar_evento(lista):
    '''
    nome = input('Digite o nome do evento: ')
    dia = input('Digite o dia do evento: ')
    hora = input('Digite a hora do evento: ')
    local = input('Digite o local do evento: ')
    evento = {'nome': nome, 'data': dia, 'hora': hora, 'local': local}
    '''
    novos_eventos = [
        {'nome': 'Olha! Recife Noturno:', 'data': '01/10/2024', 'hora': '21:00', 'local': 'Tour Histórico'},
        {'nome': 'Olha! Recife Pedalando:', 'data': '29/09/2024', 'hora': '09:00', 'local': 'Antigos Cinemas do Recife'},
        {'nome': 'Olha! Recife Barco:', 'data': '26/09/2024', 'hora': '12:00', 'local': 'Passeio no Capibaribe'},
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
    '''
    return lista
    

# Função para alterar data/hora de um evento
def alterar_evento(lista):
    '''
    evento_antigo = input('Digite o nome, o dia, a hora e o local do evento que deseja alterar (formato: nome: dd/mm/aaaa hh:mm local): ')

    novo_dia = input('Digite o novo dia do evento (formato: dd/mm/aaaa): ')
    nova_hora = input('Digite a nova hora do evento (formato: hh:mm): ')
    novo_local = input('Digite o novo local do evento: ')

    for evento in lista:
        # Verifica se o nome, dia e hora do evento correspondem ao evento antigo
        if evento['nome'] + ': ' + evento['data'] + ' ' + evento['hora'] + ' ' + evento['local'] == evento_antigo:
            # Atualiza os detalhes do evento
            evento['data'] = novo_dia
            evento['hora'] = nova_hora
            evento['local'] = novo_local
            print('Evento alterado com sucesso!')
            return lista

    # Se o evento não for encontrado, informa ao usuário
    print('Evento não encontrado.')
    '''
    return lista

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
    # Verificar o comprimento das duas listas
    if len(lista_inicial) != len(lista_atual):
        return True
    
    # Caso os tamanhos forem iguais, comparar cada evento das duas listas
    for evento_inicial, evento_atual in zip(lista_inicial, lista_atual):
        if evento_inicial != evento_atual:
            return True
    
    return False

def main():
    # Lista de dicionários para cada evento inicial
    lista_inicial = [
        {'nome': 'Olha! Recife a Pé:', 'data': '27/09/2024', 'hora': '09:30', 'local': 'Recife Walking Tour'},
        {'nome': 'Olha! Recife no Rio:', 'data': '28/09/2024', 'hora': '09:00', 'local': 'Ilha de Deus'},
        {'nome': 'Olha! Recife de Ônibus:', 'data': '28/09/2024', 'hora': '09:00', 'local': 'Jardim Botânico'},
        {'nome': 'Olha! Recife de Ônibus:', 'data': '28/09/2024', 'hora': '14:00', 'local': 'Instituto Ricardo Brennand'},
        {'nome': 'Olha! Recife de Ônibus:', 'data': '29/09/2024', 'hora': '13:00', 'local': 'Fundação Gilberto Freyre'},
        {'nome': 'Olha! Recife Pedalando:', 'data': '29/09/2024', 'hora': '09:00', 'local': 'Antigos Cinemas do Recife'},
        {'nome': 'Olha! Recife a Pé:', 'data': '02/10/2024', 'hora': '14:00', 'local': 'Pátio do Terço e Arredores'},
        {'nome': 'Olha! Recife a Pé:', 'data': '04/10/2024', 'hora': '09:30', 'local': 'Recife Walking Tour'},
    ]
    
    # Fazer uma cópia da lista inicial para evitar alterações indesejadas
    lista_inicial_copia = copy.deepcopy(lista_inicial)
    
    # Adicionar novos eventos
    lista_nova = adicionar_evento(lista_inicial)

    # Verificar se houve mudanças na lista
    if houve_mudanca(lista_inicial_copia, lista_nova):
        
        """ print("Lista original:")
        for evento in lista_nova:
            print(evento)  """
        
            
        # Medir o tempo de execução de cada algoritmo
        start_time = time.time()
        lista_nova_merge = metodo_ordenacao(lista_nova, 'mergesort')
        tempo_merge = time.time() - start_time

        start_time = time.time()
        lista_nova_quick = metodo_ordenacao(lista_nova, 'quicksort')
        tempo_quick = time.time() - start_time

        start_time = time.time()
        lista_nova_heap = metodo_ordenacao(lista_nova, 'heapsort')
        tempo_heap = time.time() - start_time

        
        """ print("\nLista ordenada com Merge Sort:")
        for evento in lista_nova_merge:
            print(evento)

        print("\nLista ordenada com Quick Sort:")
        for evento in lista_nova_quick:
            print(evento)

        print("\nLista ordenada com Heap Sort:")
        for evento in lista_nova_heap:
            print(evento)  """
        
            
        print(f"Tempo de execução do Merge Sort: {tempo_merge:.6f} segundos")
        print(f"Tempo de execução do Quick Sort: {tempo_quick:.6f} segundos")
        print(f"Tempo de execução do Heap Sort: {tempo_heap:.6f} segundos")
        
    else:
        print("Não houve mudanças na lista de eventos.")

if __name__ == "__main__":
    main()