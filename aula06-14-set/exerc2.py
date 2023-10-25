from biblioteca import lista

def pega_notas(pessoa):
    nota = pessoa['notas']
    if type(nota) == int: notas = [notas]
    return notas

def mostrar_valores():
    for p in lista:
        trabs = len(pega_notas(p))
        print(f"{p['nome']} entregou:{trabs} trabalhos")

mostrar_valores()
