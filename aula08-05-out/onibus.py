from bibliotecaPessoas import carro

def listar_pessoas():
    print('Lista de pessoas no carro:')
    for p in carro:
        print(f'Nome: {p["nome"]}\nIdade: {p["idade"]} \nPoltrona: {p["poltrona"]}\n')
listar_pessoas()

def captura_info():
    nome = input('Nome: ')
    idade = int(input('Idade: '))

    poltronas_ocupadas = carro[1]['poltrona']
    print(f'\nAgora escolha uma poltrona, as poltronas ocupadas são: {poltronas_ocupadas}')

    poltrona = int(input('Poltrona: '))
    if poltrona == poltronas_ocupadas:
        poltrona.append(poltrona)
            
    else: print('Poltrona ocupada, escolha uma poltrona disponível')
    return nome, idade, poltrona

captura_info()

# def poltronas_oc(carro):
#     for p, a in zip(poltrona, carro):