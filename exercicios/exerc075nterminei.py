# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

soma = 0
for v in range(4):
    valor = int(input('Digite um valor: '))
    soma += valor

print(f'A soma dos valores é: {soma}\n a posição do nº 5 é: {v.count(5)}')
