# Mostrar quem teve maior média, considerando todas provas dadas;

from biblioteca import lista

novapessoa = {
    'nome': 'Elvis',
    'notas': [70, 100],
}

lista.append(novapessoa)

lista_maior = []
nomes_maior = []

for pessoa in lista:
    notas = pessoa['notas']
    if type(notas) == int: notas = [notas]
    soma = float(sum(notas))
    tam = len(notas)
    media = soma/tam
    nome = pessoa['nome']

    if len(lista_maior) > 0:
        maior = lista_maior[0]
    else: 
        maior = 0

    if media == maior:
        lista_maior.append(media)
        nomes_maior.append(nome)
    elif media > maior:
        lista_maior = []
        nomes_maior = []
        lista_maior.append(media)
        nomes_maior.append(nome)

print(f'A maior media é: {lista_maior}, {nomes_maior}')