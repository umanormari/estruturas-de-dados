#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

nome = input(f'Digite seu nome: ')
print(f'Olá, sr(a) {nome}, daremos andamento no seu antendimento, mas antes, por favor, nos responda as seguintes questões:')

# def emprestimo_bancario(proposta):
v_casa = float(input(f'Qual é o valor do imóvel? R$ '))
salario = float(input(f'Qual é o valor do seu salário? R$ '))
anos = int(input(f'Em quantos anos você pretende pagar? '))

calcula_prestacao = v_casa / (anos * 12)

if calcula_prestacao >= salario * 30 / 100:
    print(f'Para pagar uma casa de {v_casa} em {anos} a prestação será {calcula_prestacao}, seu empréstimo bancário foi ACEITO!')
else:
    print(f'Para pagar uma casa de {v_casa} em {anos} a prestação será {calcula_prestacao}, seu empréstimo bancário foi NEGADO!')

print(f'Seu salário é: {salario}, o valor do imóvel é: {v_casa}, e a quantidade de anos para o pagamento é: {anos}')
