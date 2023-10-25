# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# while True:
#     escolha = int(input('Escolha um numero de 0 a 20:\n'))
#     if 0 <=escolha <=20:
#         break
#     print('Tente novamente.')
# print(f'Você digitou o número: {num[escolha]}')


num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = int(input('Escolha um numero de 0 a 20:\n'))
    escolha2 = int(input('Escolha outro um numero de 0 a 20:\n'))
    if 0 <=escolha <=20:
        break
    print('Tente novamente.')
print(f'O intervalo de numeros que você selecionou foi: {num[escolha:escolha2+1]}')