from construcao_logica import *

#  Função principal
def main():
    list_options()
    
main()























# VERSÃO MARIANA

# def listar_infos():
#     def pessoas():
#         for pessoa in lista_pessoas:
#             nome = pessoa['nome']
#             idade = pessoa['idade']
#             documento = pessoa['documento']
#             telefone = pessoa['telefone']
#             email = pessoa['email']
#             print(pessoa)

#     def assentos():
#         for assento in lista_assentos:
#             lugar = assento['tipo']
#             numeracao = assento['numeracao']
#             print(assento)

#     def bilhetes():
#         for bilhete in lista_bilhetes:
#             data = bilhete['data']
#             horario = bilhete['horario']
#             origem = bilhete['origem']
#             destino = bilhete['destino']
#             print(bilhetes)

#     pprint.pprint(pessoas())
#     pprint.pprint(assentos())
#     pprint.pprint(bilhetes())



#  VERSÃO RENAN
# def listar_infos():

#     for pessoa in lista_pessoas:

#         # INFOS DA PESSOA
#         nome = pessoa['nome']
#         idade = pessoa['idade']
#         documento = pessoa['documento']
#         telefone = pessoa['telefone']
#         email = pessoa['email']

#         # INFOS DO ASSENTO
#         for assento in lista_assentos:
#             lugar = assento['tipo']
#             numeracao = assento['numeracao']


#         # INFOS DO BILHETE / VIAGEM
#         for bilhete in lista_bilhetes:
#             data = bilhete['data']
#             horario = bilhete['horario']
#             origem =  bilhete['origem']
#             destino = bilhete['destino']


#     info_pessoa = {
#         'nome': nome,
#         'idade': idade,
#         'documento': documento,
#         'telefone': telefone,
#         'email': email,
#     }


#     info_assento = {
#         'lugar' : lugar,
#         'numeracao' : numeracao
#     }

#     info_bilhete = {
#         'data' : data,
#         'horario' : horario,
#         'origem' : origem,
#         'destino' : destino
#     }

#     info_totais = {
#         'infosPessoa' : info_pessoa,
#         'infosAssento' : info_assento,
#         'infosBilhete' : info_bilhete
#     }

#     pprint.pprint(info_totais)