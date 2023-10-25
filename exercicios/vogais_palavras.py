palavras = ('casa', 'carro', 'caneta', 'computador', 'livro', 'chave', 'telefone', 'cadeira', 'janela', 'mesa')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')