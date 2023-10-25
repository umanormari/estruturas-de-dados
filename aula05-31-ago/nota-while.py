from biblioteca import lista

def captura_info():  
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    # Aqui a variavel irá receber uma lista↓
    notas = []  

    # O laço de repetição vai pedir 3 notas, e adicionar em 'notas' em formato de LISTA
    while len(notas) < 3:
        tmp = int(input('Digite sua nota: '))
        if tmp == 'abcdefghijklmnopqrstuvxyz@#$%':
            print('Você digitou errado, digite um valor')
            break   
        notas.append(tmp)
    
    registro = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }
    return registro

p4 = captura_info()
lista.append(p4)
print(p4)