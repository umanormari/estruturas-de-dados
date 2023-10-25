# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

from time import sleep

times = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Vasco da Gama', 'América-MG')


print(f'Os 5 primeiros colocados são:\n{times[:6]}')
print('=-' * 15)
sleep(0.5)

print(f'Os ultimos 4 colocados são:\n{times[-4:]}')
print('=-' * 15)
sleep(0.5)

print(f'Os times em ordem alfabética:\n{sorted(times)}') 
print('=-' * 15)
sleep(0.5)

print(f'O Coritiba está na {times.index("Coritiba")+1} ª posição')
