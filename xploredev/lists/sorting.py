def insertion_sort(arr):

    # criando uma copia do array para nao modificar o original
    arr = arr.copy()

    # varre todo o array a comecar do segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # empurra os elementos anteriores do key no array que sao maiores que a chave
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # atribui a chave na posicao correta
        arr[j + 1] = key

    return arr
