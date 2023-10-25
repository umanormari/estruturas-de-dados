frase = input('Digite uma frase: ')
palavra_antiga = input(f'Digite a palavra que você deseja substituir: ')
palavra_nova = input(f'Digite uma palavra para substituir por {palavra_antiga}: ')

substitui = frase.replace(palavra_antiga, palavra_nova)

print(f'Sua nova frase é: {substitui}')