everyone = []
print('-=' * 15)
print('{:^30}'.format('CADASTRADOR DE PESSOAS'))
print('-=' * 15)
while True:
    n = []
    name = str(input('Nome: ')).strip().title()
    n.append(name)
    age = int(input('Idade: '))
    n.append(age)
    gender= ' '
    while gender not in 'MmFf':
        gender = str(input('Sexo: [M/F]')).strip()
        n.append(gender)
    everyone.append(n[:])
    sn = ' '
    while sn not in 'SsNn':
        sn = str(input('Quer Continuar? [S/N]')).strip()
    if sn in 'Nn':
        break
for c in everyone:
    print('-=' * 15)
    print(f'''Nome:           {c[0]}
Idade:          {c[1]} anos
Sexo:           {c[2].upper()}''')
print('-=' * 15)