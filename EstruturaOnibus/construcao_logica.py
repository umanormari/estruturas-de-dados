# Import das libs (json e pprint) para formatar do jeito que eu quero apresentar minhas informações do dicionário
# Deixar meu dicionário de uma forma mais legível em formato JSON
import json
import pprint

from lib import lista_pessoas, lista_assentos, lista_bilhetes

# Funçao para adicionar um novo passageiro
def add_person():
    print()
    name = input("Informe o nome do passageiro: ")
    idade = int(input("Informe a idade do passageiro: "))
    documento = input("Informe o documento do passageiro: ")
    telefone = input("Informe o número de telefone do passageiro: ")
    email = input("Informe o email do passageiro: ")

    assento = option_seat()

    new_person = {
        'nome': name,
        'idade': idade,
        'documento': documento,
        'telefone': telefone,
        'email': email,
    }

    lista_pessoas.append(new_person)

    new_seat = {
        'pessoa': new_person,
        'numeracao': 4,
        'tipo': assento,
        'custo': 150,
    }

    lista_assentos.append(new_seat)

    # Realizar a parte do bilhete

    # bilhete5 = {
    #     'pessoa': lista_assentos[4]['pessoa']['nome'],
    #     'assento': lista_assentos[4]['numeracao'],
    #     'tipo': lista_assentos[4]['tipo'],
    #     'data': '02/10/2023',
    #     'horario': '11:00',
    #     'origem': 'Curitiba',
    #     'destino': 'Rio de Janeiro',
    #   }

    #       APPEND NA LISTA DE BILHETES

# Função para escolher as opções de assentos (Leito, semileito ...)


def option_seat():
    opcao = input("Informe o tipo de assento que deseja: ")
    assento = 0

    match opcao:
        case 'Executivo':
            assento = 'Executivo'

        case 'Semi-leito':
            assento = 'Semi-leito'

        case 'Leito':
            assento = 'Leito'

        case 'Leito-cama':
            assento = 'Leito-cama'
    return assento

# Função para listar todos os passageiros
def listar_pessoas():
    for bilhetes in lista_bilhetes:
        print(f"As pessoas a bordo do ônibus são: --> {bilhetes['pessoa']}")

#  Função para calcular custo total
def calcular_custo_total(assentos):

    custo_total = 0
    for assento in assentos:
        if assento['pessoa']['nome'] != 'NULL':
            custo_total += assento['custo']
    return custo_total

# Função para apresentar o valor calculado
def apresentar_valor():
    custo_total = calcular_custo_total(lista_assentos)
    print(
        f"O custo total pago pelos assentos comprados é: R$ {custo_total},00")


#  Função que passo todas as listas como parametro, e de cada uma delas, pego somente algumas informações para 
#  compor somente as informações que eu quero
def listar_infos(lista_pessoas, lista_assentos, lista_bilhetes):
    info_totais = []

    for pessoa in lista_pessoas:
        # INFOS DA PESSOA
        nome = pessoa['nome']
        idade = pessoa['idade']
        documento = pessoa['documento']
        telefone = pessoa['telefone']
        email = pessoa['email']

        for assento in lista_assentos:
            lugar = assento['tipo']
            numeracao = assento['numeracao']

        for bilhete in lista_bilhetes:
            data = bilhete['data']
            horario = bilhete['horario']
            origem = bilhete['origem']
            destino = bilhete['destino']

        info_pessoa = {
            'nome': nome,
            'idade': idade,
            'documento': documento,
            'telefone': telefone,
            'email': email,
        }

        info_assento = {
            'lugar': lugar,
            'numeracao': numeracao
        }

        info_bilhete = {
            'data': data,
            'horario': horario,
            'origem': origem,
            'destino': destino
        }

        info_totais({
            'infosPessoa': info_pessoa,
            'infosAssento': info_assento,
            'infosBilhete': info_bilhete
        })

    pprint.pprint(info_totais)

# Função para mostrar o menu de opções do nosso sistema de gerencimanento de ônibus
def list_options():
    print("                                                       SGO - SISTEMA GERENCIADOR DE ÔNIBUS                                             ")

    print()
    print(" _____________ TABELA DE OPÇÕES _____________")
    print("                                             ")
    print("       ADD PASSAGEIRO        (1)             ")
    print("       APRESENTAR VALORES    (2)             ")
    print("       LISTAR PESSOAS        (3)             ")
    print("       LISTAR TOTAL INFOS    (4)             ")
    print("_____________________________________________")

    print()
    opcao = int(input(" INFORME UMA DAS OPÇÕES ACIMA QUE DESEJA OPERAR: "))

    match opcao:
        case 1:
            add_person()

            print()
            print(" ------------ LISTA DE PESSOAS ------------- ")
            print(json.dumps(lista_pessoas, sort_keys=False, indent=5))

            print()

            print(" ------------ LISTA DE ASSENTOS  ------------- ")
            print(json.dumps(lista_assentos, sort_keys=False, indent=5))
            print(" ------------------------------------------- ")

        case 2:
            apresentar_valor()

        case 3:
            listar_pessoas()

        case 4:
            listar_infos(lista_pessoas, lista_assentos, lista_bilhetes)