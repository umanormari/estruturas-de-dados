# Mostrar quem teve menor média trabalhos dados

from biblioteca import lista

menor = 99999999
nome_menor = ''

tamanho = 3

for p in lista:
    nota = p['notas']
    if type(nota) == int: nota = [nota]
    soma = sum(nota)
    media = soma/tamanho
    if media < menor:
        menor = media
        nome_menor = p['nome']

print(f'A menor media é: {menor}, o nome da pessoa é: {nome_menor}')