from biblioteca import lista

def pega_notas(pessoa):
    nota = pessoa['notas']
    if type(nota) == int: notas = [notas]
    return notas

def mostrar_med_trab():
    contar = 0
    for p in lista:
        contar = contar + len(p['notas'])
    resultado = contar / len(lista)

    print(f"A media de notas é: {resultado}")

mostrar_med_trab()