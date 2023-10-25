# LISTAS COMPOSTAS:
# pessoas = [['Pedro',25]['Maria',19]['João',32]]
# print(pessoas[1][1])

trabalho = list()
trabalho.append('Mariana')
trabalho.append(27)

amigos = list()
amigos.append(trabalho[:])
trabalho[0] = 'Abner'
trabalho[1] = 28

# É NECESSÁRIO USAR UM SLICE PARA PODER FAZER UMA CÓPIA CASO QUEIRA JOGAR UMA LISTA NA OUTRA
amigos.append(trabalho[:]) 
print(amigos)