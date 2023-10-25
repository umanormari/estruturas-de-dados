# Mostrar quem teve maior média, considerando somente provas dadas;
from biblioteca import lista

maior = 0
nome_maior = ''

tamanho = 3

for pessoa in lista:
    nota = pessoa['notas']
    if type(nota) == int: nota = [nota]
    soma = sum(nota)
    media = soma/tamanho
    if media > maior:
        maior = media
        nome_maior = pessoa['nome']

print(f'a maior media é de provas dadas é: {maior} e o nome da pessoa é: {nome_maior}')