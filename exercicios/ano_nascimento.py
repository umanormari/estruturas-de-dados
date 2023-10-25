# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

data_atual = 2023 
ano_nasc = int(input('Insira o ano de seu nascimento: '))
idade = data_atual - ano_nasc
idade_alistamento = 18
print(f'Você nasceu em {ano_nasc}, sua idade é {idade} anos em {data_atual}')

if idade == idade_alistamento: 
    print('Você deve se alistar ao serviço militar IMEDIATAMENTE!')

elif idade < idade_alistamento:
    falta = idade_alistamento - idade
    print(f'Ainda faltam {falta} anos para você se alistar ao serviço militar!')

else:
    print('Já passou da hora de se alistar serviço militar!')