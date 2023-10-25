from biblioteca import lista

def achar_menor_nota():
    menor = 9999
    for p in lista:
        notas = p['notas']
        for num in notas:
            if num < menor:
                menor = num
    print(f'A menor nota da lista é: {menor}')

achar_menor_nota()