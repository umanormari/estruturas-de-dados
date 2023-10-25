# Mostrar quem teve maior nota

from biblioteca import lista

maior = 0
nome_maior = ''

tamanho = 3

for p in lista:
    nota = p['notas']
    if type(nota) == int: nota = [nota]
    maior_nota = max(nota)
    if maior_nota > maior:
        maior = maior_nota
        nome_maior = p['nome']

print(f'Quem tirou a maior nota foi: {nome_maior}, com {maior}')