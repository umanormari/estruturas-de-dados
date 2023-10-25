# frase = input('Digite uma frase: ')
# letra = input('Escolha uma letra para contagem: ')

# quant = frase.count(f'{letra}')
# print(f'Sua frase tem {quant} letras {letra}')

frase2 = input('Digite uma frase: ')
letra2 = input('Escolha uma letra para contagem de uma parte da frase digitada: ')

parte_frase = frase2.count(letra2,2,16)
print(f'Sua frase tem {parte_frase} letras {letra2}')