# frase = input('Digite seu e-mail: ')

# tmp, dominio = frase.split('@')
# user = tmp
# print(f'Seu usuário é: {user} \n e seu dominio é {dominio}')

#agora cada palavra vira um indice, e o numero que o usuario digitar irá capturar a palavra conforme sua posição, ex: 'hoje o dia esta quente', [2], saída: 'dia'
frase = input('Digite uma frase: ')
num = int(input('Digite um numero: '))
frase_nova = frase.split()
print('A palavra escolhida é:', frase_nova[num])