# Merge Sort: algoritmo obtido no conteúdo da Trybe


def merge_sort(words, start=0, end=None):
    if end is None:
        end = len(words)

    # se não reduzi o suficiente, continua
    if (end - start) > 1:
        # encontrando o meio
        mid = (start + end) // 2
        # dividindo as listas
        merge_sort(words, start, mid)
        merge_sort(words, mid, end)
        # unindo as listas
        merge(words, start, mid, end)

# Função auxiliar que realiza a mistura dos dois arrays


def merge(words, start, mid, end):
    left = words[start:mid]   # indexando a lista da esquerda
    right = words[mid:end]   # indexando a lista da direita

    left_index, right_index = 0, 0   # as duas listas começarão do início

    # percorrer sobre a lista inteira como se fosse uma
    for general_index in range(start, end):
        # se os elementos da esquerda acabaram, preenche com a lista da direita
        if left_index >= len(left):
            words[general_index] = right[right_index]
            right_index = right_index + 1

        # se os elementos da direita acabaram, preenche com a lista da esquerda
        elif right_index >= len(right):
            words[general_index] = left[left_index]
            left_index = left_index + 1

        # se o elemento do topo da esquerda for < o da direita, será escolhido
        elif left[left_index] < right[right_index]:
            words[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            # caso o da direita seja menor, ele será o escolhido
            words[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    # converte as strings para minúsculas e transforma em listas de caracteres
    first_list_characters = list(first_string.lower())
    second_list_characters = list(second_string.lower())

    # organiza as listas em ordem alfabética
    merge_sort(first_list_characters)
    merge_sort(second_list_characters)

    # converte as listas ordenadas de volta para strings
    sorted_first_string = "".join(first_list_characters)
    sorted_second_string = "".join(second_list_characters)

    # verifica se as strings ordenadas são iguais
    if sorted_first_string and sorted_second_string:
        are_anagrams = sorted_first_string == sorted_second_string
    else:
        are_anagrams = False

    return (sorted_first_string, sorted_second_string, are_anagrams)
