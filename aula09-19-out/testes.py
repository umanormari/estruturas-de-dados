from biblioteca import lista_pessoas, lista_assentos, lista_bilhetes

# MOSTRANDO A LISTA DE PESSOAS
for bilhetes in lista_bilhetes:
    print(f"As pessoas a bordo do ônibus são: --> {bilhetes['pessoa']}")

# CALCULANDO VALORES
def calcular_custo_total(assentos):
    custo_total = 0
    for assento in assentos:
        if assento['pessoa']['nome'] != 'NULL':
            custo_total += assento['custo']
    return custo_total

custo_total = calcular_custo_total(lista_assentos)

print(f"O custo total pago pelos assentos comprados é: R$ {custo_total},00")

# INSERINDO NOVA PESSOA NO ONIBUS
# def gerar_bilhete(lista_assentos):
#     reserva = ''
#     for assento in lista_assentos:
#         if lista_assentos[0]['pessoa']['nome'] == 'NULL':
#             reserva['nome'] = input('Digite seu nome: ')
#             reserva['idade'] = input('Digite sua idade: ')
#             reserva['documento'] = input('Digite seu documento: ')
#             reserva['telefone'] = input('Digite seu telefone: ')
#             reserva['email'] = input('Digite seu e-mail: ')
#             reserva = assento
#             break
        
#         else: reserva != 'Null'
#         print('Infelizmente não há mais disponibilidade nesta viagem!')
#         return
#     return reserva

# gerar_bilhete(lista_assentos)
