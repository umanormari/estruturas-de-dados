print(f'Bem Vindo! O Mercadão agradece por ser nosso cliente\n')

valor = float(input('Digite o valor de seu produto para aplicarmos um desconto de 5%:'))
produto = valor * 5 / 100
preco_final = valor - produto

print(f"Certo, aqui está o valor com o desconto aplicado {preco_final}")