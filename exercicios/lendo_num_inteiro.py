# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero: '))

base = int(input(f'Escolha uma base de conversõo:\n → 1 - Binário\n → 2 - Octal\n → 3 - Hexadecimal\n Base: '))

if base == 1: print(f'{num} convertido para Binário é: {bin(base)}')
elif base == 2: print(f'{num} convertido para Octal é: {oct(base)}')
elif base == 3: print(f'{num} convertido para Hexadecimal é: {hex(base)[2:]}')
else: print(f'Esta opção esta inválida')

# encontra_base()