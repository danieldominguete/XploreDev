def insertion_sort(elements: list) -> list:

    # Complexidade de tempo: O(n^2) no pior caso
    # Complexidade de espaco: O(1)

    # criando uma copia do array para nao modificar o original
    elements = elements.copy()

    # varre todo o array a comecar do segundo elemento
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        # empurra os elementos anteriores do key no array que sao maiores que a chave
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        # atribui a chave na posicao correta
        elements[j + 1] = key

    return elements


def merge_sort(elements: list) -> list:
    # Complexidade de tempo: O(n log n) em todos os casos
    # Complexidade de espaco: O(n)

    # criando uma copia do array para nao modificar o original
    elements = elements.copy()

    # se o array tiver 1 ou nenhum elemento, ja esta ordenado
    if len(elements) <= 1:
        return elements

    # encontra o ponto medio do array
    mid = len(elements) // 2

    # divide o array em duas metades e ordena recursivamente
    left_half = merge_sort(elements[:mid])
    right_half = merge_sort(elements[mid:])

    # mescla as duas metades ordenadas
    return merge(left_half, right_half)


def merge(left: list, right: list) -> list:
    merged_array = []
    left_index = 0
    right_index = 0

    # compara os elementos das duas metades e adiciona o menor ao array ordenado
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    # adiciona os elementos restantes da metade esquerda, se houver
    while left_index < len(left):
        merged_array.append(left[left_index])
        left_index += 1

    # adiciona os elementos restantes da metade direita, se houver
    while right_index < len(right):
        merged_array.append(right[right_index])
        right_index += 1

    return merged_array


def quick_sort(elements: list) -> list:
    # Complexidade de tempo: O(n log n) no caso medio, O(n^2) no pior caso
    # Complexidade de espaco: O(log n)

    # criando uma copia do array para nao modificar o original
    elements = elements.copy()

    if len(elements) <= 1:
        return elements

    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    middle = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for cap in range(1, capacity + 1):
            if w <= cap:
                dp[i][cap] = max(dp[i - 1][cap], dp[i - 1][cap - w] + v)
            else:
                dp[i][cap] = dp[i - 1][cap]

    return dp[n][capacity]
