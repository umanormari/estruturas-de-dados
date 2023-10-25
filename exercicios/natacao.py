# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

data_atual = 2023 
ano_nasc = int(input('Insira o ano de seu nascimento: '))
idade = data_atual - ano_nasc

if idade <= 9: 
    print(f'Você tem {idade} anos, sua categoria é: MIRIM!')
if idade <= 14: 
    print(f'Você tem {idade} anos, sua categoria é: INFANTIL!')
if idade <= 19: 
    print(f'Você tem {idade} anos, sua categoria é: JÚNIOR!')
if idade <= 25: 
    print(f'Você tem {idade} anos, sua categoria é: SÊNIOR!')
if idade >= 25: 
    print(f'Você tem {idade} anos, sua categoria é: MASTER!')