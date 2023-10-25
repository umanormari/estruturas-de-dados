from biblioteca import lista

novapessoa = {
    'nome': 'Elvis',
    'notas': [70, 100],
}

lista.append(novapessoa)

soma_turma = 0
total_notas_turma = 0

for pessoa in lista:
    notas = pessoa['notas']

    if isinstance(notas, int):  
        notas = [notas]

    soma = sum(notas)
    total_notas_turma += len(notas)
    soma_turma += soma
    
    nome = pessoa['nome']
    media = soma / len(notas)

media_turma = soma_turma / total_notas_turma
print(f"Média da turma com base nas notas feitas é: {media_turma}")


# tam = 0
# soma = 0
# for pessoa in lista:
#     notas = pessoa['notas']

#     if type(notas) == int: notas = [notas]
    
#     soma = float(sum(notas))
#     soma += soma
#     tam += len(notas)
#     media = soma/tam

# print(f' A média da turma é: {media}')