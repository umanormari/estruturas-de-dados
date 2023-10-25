from biblioteca import lista

# def achar_maior_nota():
#     maior = 0
#     for p in lista:
#         notas = p['notas']
#         for num in notas:
#             if num > maior:
#                 maior = num
#     print(f'A menor nota da lista é: {maior}')

# def achar_maior_nota_pessoa():    
#     for p in lista:
#         maior = -1
#         notas = p['notas']
#         for num in notas:
#             if num > maior:
#                 maior = num
#         print(f'A maior nota da lista é: {maior}')

# def achar_menor_pessoa():    
#     for p in lista:
#         menor = 9999
#         notas = p['notas']
#         for num in notas:
#             if num < menor:
#                 menor = num
#         print(f'A menor nota da lista é: {menor}')

def acrescentar_nota(lista):
    for p, n in zip(lista, notas):
        p['notas'].append(n)
acrescentar_nota(8, 10)

# def listar_notas():
#     print('Listando Notas:', )
#     for p in lista:
#         print(f'{p["nome"]} Notas:' {notas["notas"]})