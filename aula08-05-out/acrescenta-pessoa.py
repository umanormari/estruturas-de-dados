from biblioteca import lista

def inserir_pessoa(nome, idade, notas):
    novo = {
        'nome' = nome,
        'idade' = idade,
        'notas' = notas
    }

    lista.append(novo)
    

def captura_dados():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    notas = []
    for nid in range(3):
        tmp = input('Digite a nota: ')
        notas.append(notas)
    return nome, idade, notas

captura_dados(nome, idade, notas)

def codigo_teste():

    # everyone.append(n[:])
    # sn = ' '
    # while sn not in 'SsNn':
    #     sn = str(input('Quer Continuar? [S/N]')).strip()
    # if sn in 'Nn':
    #     break
