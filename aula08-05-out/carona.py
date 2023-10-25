from bibliotecaPessoas import assentos


def listar_vazia():
    for pessoa in assentos:
        if pessoa['idade'] == 0:
            print(pessoa['poltrona'], '--vazia')


def listar():
    for pessoa in assentos:
        if pessoa['idade'] == 0:
            print(pessoa['poltrona'], '--vazia')
        else:
            print(pessoa['poltrona'], 'Ocupado por:', pessoa['nome'])

def novo():
    encontrou = 0
    for poltrona in assentos:
        if poltrona['idade'] == 0:
            encontrou = poltrona
            break
    
    if encontrou == 0:
        print('Procure outra carona. Aqui está cheio!')
        return

    encontrou['nome'] = input('Novo passageiro: ')
    encontrou['idade'] = input('Idade: ')


listar_vazia()
novo()
listar_vazia()
novo()
listar()