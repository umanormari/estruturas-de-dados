# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


lado1 = int(input('Digite um tamanho para um lado do triângulo: '))
lado2 = int(input('Digite um tamanho para um lado do triângulo: '))
lado3 = int(input('Digite um tamanho para um lado do triângulo: '))

if lado1 == lado2 == lado3: print(f' Esse triangulo é EQUILÁTERO')
if lado1 == lado2 != lado3: print(f' Esse triangulo é ISÓSCELES')
if lado1 != lado2 != lado3: print(f' Esse triangulo é ESCALENO')
