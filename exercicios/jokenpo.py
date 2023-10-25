from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input(f'Escolha um item:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ]TESOURA\n'))

print('-=' * 11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(0.5)
print('-=' * 11)
print(f'O jogador jogou: {itens[jogador]}')
print(f'O computador jogou: {itens[computador]}')
print('-=' * 11)

if computador == 0:
    if jogador == 0: print('Empate')
    elif jogador == 1: print('O Jogador venceu')
    elif jogador == 2: print('O Computador venceu')
    else: print('Jogada inválida!')

elif computador == 1:
    if jogador == 0: print('O Computador venceu')
    elif jogador == 1: print('Empate')
    elif jogador == 2: print('O Jogador Venceu')
    else: print('Jogada inválida!')

elif computador == 2:
    if jogador == 0: print('O Computador venceu')
    elif jogador == 1: print('O Jogador Venceu')
    elif jogador == 2: print('Empate')
    else: print('Jogada inválida!')