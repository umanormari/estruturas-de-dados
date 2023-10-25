# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista = []

for v in range(5):
    valores = int(input('Digite cinco valores: '))
lista = valores.append()

print(f'Valor adicionado na posição {lista} da lista')