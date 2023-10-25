# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()

while True:
    n = int(input(f'Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor está duplicado, não pode ser adicionado!')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break

print(f'Os valores inseridos foram: {sorted(numeros)}')