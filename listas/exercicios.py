num = [5, 6, 1, 2] #lista
num[2] = 3 #substitui um numero na lista
num.append(7) #adiciona um numero no final da lista
num.sort() #coloca a lista em ordem crescente
num.sort(reverse=True) #coloca a lista em ordem decrescente
num.insert(2, 0) #insere um valor na posição determina, no exemplo, insere 0 na posição/indice 2
# num.remove(2) #remove o primeiro elemento que é escolhido
if 4 in num:
    num.remove(4) #Usando o if com o remove, o programa remove o valor somente se ele estiver na lista, evitando gerar o erro, caso o valor nao esteja
else:
    print('Não achei o número 4')

num.pop(2) #remove um indice da lista
print(num)

def achando_valor():
    valores = []
    valores.append(2)
    valores.append(4)
    valores.append(7)

    for c, v in enumerate(valores):
        print(f'Na posição {c} encontrei o valor {v}!')
# achando_valor()

def valor_encontrado():
    val = list()
    for cont in range(0, 5):
        val.append(str(input('Digite alguns nomes: ')))

    for c, v in enumerate(val):
        print(f'Na posição {c} encontrei o valor {v}!')
valor_encontrado()
