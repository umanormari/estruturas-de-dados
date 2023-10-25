# Lista de passageiros
passageiros = [
    {
        'nome': 'Maria',
        'idade': 20,
        'documento': 11112222,
        'telefone': 123456,
        'email': 'maria@email.com',
    },
    {
        'nome': 'Joao',
        'idade': 30,
        'documento': 22223333,
        'telefone': 234567,
        'email': 'joao@email.com',
    },
    {
        'nome': 'Ze',
        'idade': 50,
        'documento': 33334444,
        'telefone': 345678,
        'email': 'ze@email.com',
    },
]

# Gerar bilhetes
def gerar_bilhete(passageiro, assento):
    return {
        'pessoa': passageiro['nome'],
        'assento': assento['numeracao'],
        'tipo': assento['tipo'],
        'data': '02/10/2023',
        'horario': '11:00',
        'origem': 'Curitiba',
        'destino': 'Rio de Janeiro',
    }

# Lista de bilhetes
bilhetes = [
    gerar_bilhete(passageiros[0], {'numeracao': 1, 'tipo': 'Leito', 'custo': 200}),
    gerar_bilhete(passageiros[1], {'numeracao': 2, 'tipo': 'Leito', 'custo': 200}),
    gerar_bilhete(passageiros[2], {'numeracao': 3, 'tipo': 'Semi-leito', 'custo': 150}),
]

# Lista de pessoas a bordo
for bilhete in bilhetes:
    print(f"Pessoa a bordo: {bilhete['pessoa']}")

