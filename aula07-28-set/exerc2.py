from biblioteca import lista

def somanotas():
    soma = 0
    for p in lista:
        notas = p['notas']
        soma = soma + notas[0]
        soma = soma + notas[1]
        soma = soma + notas[2]
    print(f' As notas das pessoas da lista são: {soma}')

somanotas()