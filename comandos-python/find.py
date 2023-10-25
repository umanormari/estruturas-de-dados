frase = input('Digite uma frase: ')
busca = input('Digite o que você está buscando na frase?\n')

encontra_frase = frase.find(busca)

print(f'Sua busca está na posição: {encontra_frase}')

# Quando você procura por um valor que não existe, o resultado da busca será sempre: '-1'