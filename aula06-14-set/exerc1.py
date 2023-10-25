from biblioteca import lista

def captura_info():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
        
    registro = {
        "nome": nome,
        "idade": idade,
    }
    return registro

p4 = captura_info()
lista.append(p4)

def mostra_pessoa(lista):
    for p in lista:
        nome = p['notas']
        idade = p['idade']
print(f' A nova pessoa da lista é {lista}')