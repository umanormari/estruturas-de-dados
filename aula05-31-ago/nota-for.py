from biblioteca import lista

def captura_info():  
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    # Aqui a variavel irá receber uma lista↓
    notas = []  

    # O laço de repetição vai pedir 3 notas, e adicionar em 'notas' em formato de LISTA
    for idx in range(3):
        tmp = int(input('Digite sua nota: '))
        notas.append(tmp)

    registro = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }

    return registro


def mostrar_lista(lista): 
    for pessoa in lista:
        nome = pessoa['nome']
        idade = pessoa['idade']
        notas = pessoa['notas']
        print(f"{nome}, tem {idade} anos de idade, e suas notas foram: {notas}")

p4 = captura_info()
lista.append(p4)
mostrar_lista(lista)