#As tuplas são imutaveis

# from time import sleep

# suco  = 'laranja', 'abacaxi', 'manga', 'uva', 'maracuja', 'pessego', 'limao'

# print(f'As opções de suco são: ')
# for c in suco:
#     sleep(0.5)
#     print(c)

# #TESTE 2 - LEN
# suco  = 'laranja', 'abacaxi', 'manga', 'uva', 'maracuja', 'pessego', 'limao'

# print(f'As opções de suco são: ')
# for c in range(0, len(suco)): #A mostragem vai de 0 até o ultimo indice que está na variavel chamada.
#     print(c)


#TESTE 3 - LEN COM INDICE NO PRINT
# suco  = 'laranja', 'abacaxi', 'manga', 'uva', 'maracuja', 'pessego', 'limao'

# print(f'As opções de suco são: ')

# for c in range(0, len(suco)): #A mostragem vai de 0 até o ultimo indice que está na variavel chamada.
#     print(suco[c]) # tudo é impresso de uma só vez

# #TESTE 4 - ENUMERATE
# suco  = 'laranja', 'abacaxi', 'manga', 'uva', 'maracuja', 'pessego', 'limao'

# print(f'As opções de suco são: ')

# for pos, c in enumerate(suco):
#     print(f'{pos} - {c} ') # tudo é impresso de uma só vez e enumarado por ordem

# #TESTE 5 - SORTED
# suco  = 'laranja', 'abacaxi', 'manga', 'uva', 'maracuja', 'pessego', 'limao'
# suco2  = 1, 2, 5, 200, 8, 22, 10, 55, 20

# print(f'{sorted(suco)}') #Sorted coloca os itens da tupla em ordem alfabetica e também serve para numeros

# #TESTE 6 - INDEX
# a = (2, 5, 4)
# b =  (5, 8, 1, 2)
# c = b + a 
# print(f'{c.index(4)}') #mostra qual é a posição do numero dentro da lista, para achar mais de 1 indice, é preciso atribui + de 1 numero no parametro da busca

# TESTE 7 - Tipos diferentes na tupla

#referencia: nome, idade, sexto, peso, altura
pessoa = ('Mariana', 26, 'F', 55, 1.70)
print(pessoa)

#del(pessoa) → DELETA A TUPLA INTEIRA
