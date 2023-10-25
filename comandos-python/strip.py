#'Strip' remove todos os espaços inuteis de uma strig, como duplos espaços, somente no inicio e no final

# frase = input('Digite uma frase: ')
# remove_espaco = frase.strip()

# print(f'Sua nova frase é: {remove_espaco}')

frase = input('Digite uma frase: ')
remove_espaco = frase.rstrip()

print(f'Sua nova frase é: {remove_espaco}')

# O 'r' ao lado do 'strip' significa que tudo o que estiver ao lado 'right = direito' será removido, o final, a mesma coisa com left
