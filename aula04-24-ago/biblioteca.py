pessoa1 = {
    'nome': 'Anna',
    'idade': 22,
    'altura': 1.70,
    'trab-entregues': 1,
    'datas-entrega': '15-02',
    'notas': 80,
}

pessoa2 = {
    'nome': 'Bob',
    'idade': 18,
    'altura': 1.80,
    'trab-entregues': 2,
    'datas-entrega': ('16-02', '30-02'),
    'notas': (90, 60),
}

pessoa3 = {
    'nome': 'Carl',
    'idade': 28,
    'altura': 1.65,
    'trab-entregues': 3,
    'datas-entrega': ('14-02', '20-02', '01-03'),
    'notas': (60, 40, 80),
}
pessoa4 = {
    'nome': 'Daniel',
    'notas': [70, 100],
}

lista = [pessoa1, pessoa2, pessoa3]
lista.append(pessoa4)

media_a = pessoa1['notas']

notas = pessoa2['notas']
media_b = (notas[0]+notas[1])/2

notas = pessoa3['notas']
media_c = (notas[0]+notas[1]+notas[2])/3

notas = pessoa4['notas']
media_d = (notas[0]+notas[1])/2

print('Ana, media:', media_a)
print('Bob, media:', media_b)
print('Carl, media:', media_c)
print('Daniel, media:', media_d)