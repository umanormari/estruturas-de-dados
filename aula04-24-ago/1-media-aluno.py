# Fazer a Média de cada aluno;

from biblioteca import lista

# notas1 = pessoa1['notas']
# media1 = notas1 / notas1

# notas2 = pessoa2['notas']
# media2 = (notas2[0] + notas2[1])/2

# notas3 = pessoa3['notas']
# media3 = sum(notas3) / len(notas3)


# print(f'A média da Anna é: {media1}\n a média do Bob é: {media2}\n a média do Carl é: {media3}')

for pessoa in lista:
    notas = pessoa['notas']

    if type(notas) == int: 
        notas = [notas]

    soma = float(sum(notas))
    tam = len(notas)
    media = soma/tam
    nome = pessoa['nome']
print(f"{nome}, média = {media}")