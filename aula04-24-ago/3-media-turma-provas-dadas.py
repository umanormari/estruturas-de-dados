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

    # if media > maior:
    #     maior = media
    #     nome_maior = pessoa['nome']

print(f"Média da turma com base nas notas feitas é: {media}")

# Anna   80 / 3 = 26,66
# Bob     90+60 = 150 / 3 = 50
# Carl 60+40+80 = 180 / 3 = 60
# Daniel 70+100 = 170 / 3 = 56,6

# SOMA DAS MÉDIAS: 193,26

