from biblioteca import lista

# def captura_info():
#     nome = input('Digite seu nome: ')
#     idade = int(input('Digite sua idade: '))
        
#     registro = {
#         "nome": nome,
#         "idade": idade,
#     }
#     return registro

# p5 = captura_info()


# def parte1():
#     nota = lista[1]['notas'][1]
# print(f' A nota da pessoa 2 é: {notas}')

def mostra_pessoa():
    for p in lista:
        notas = p['notas']
    return notas
    
print(f' As notas das pessoas da lista são: {mostra_pessoa}')

mostra_pessoa()

