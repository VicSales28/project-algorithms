def find_duplicate(nums: list[int]):
    # ordena a lista para facilitar a detecção de duplicatas
    nums.sort()

    # itera pela lista a partir do segundo elemento
    for i in range(1, len(nums)):
        # verifica se o elemento atual é uma string ou negativo
        if isinstance(nums[i], str) or nums[i] < 0:
            return False
        # verifica se o elemento atual é igual ao elemento anterior
        if nums[i] == nums[i - 1]:
            # se encontrar uma duplicata, retorna o valor duplicado
            return nums[i]
    # se nenhuma duplicata for encontrada, retorna False
    return False
