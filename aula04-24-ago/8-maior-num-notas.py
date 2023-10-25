from biblioteca import lista

maior = 0
nome_maior = ''


for p in lista:
    nota = p['notas']
    if type(nota) == int: nota = [nota]
    contar = len(nota)

    if contar > maior:
        maior = contar
        nome_maior = p['nome']

print('Quem fez a maior quantidade de trabalhos foi: {nome_maior}, com {maior} trabalhos feitos')