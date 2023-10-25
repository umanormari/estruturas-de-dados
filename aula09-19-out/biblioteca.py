p1 = {
    'nome': 'Maria',
    'idade': 20,
    'documento': 11112222,
    'telefone': 123456,
    'email': 'maria@email.com',
}

p2 = {
    'nome': 'Joao',
    'idade': 30,
    'documento': 22223333,
    'telefone': 234567,
    'email': 'joao@email.com',
}

p3 = {
    'nome': 'Ze',
    'idade': 50,
    'documento': 33334444,
    'telefone': 345678,
    'email': 'ze@email.com',
}

p4 = {
    'nome': 'NULL',
    'idade': 'NULL',
    'documento': 'NULL',
    'telefone': 'NULL',
    'email': 'NULL',
}

p5 = {
    'nome': 'NULL',
    'idade': 'NULL',
    'documento': 'NULL',
    'telefone': 'NULL',
    'email': 'NULL',
}

lista_pessoas = [p1, p2, p3, p4, p5]

assento1 = {
    'pessoa': lista_pessoas[0],
    'numeracao': 1,
    'tipo': 'Leito',
    'custo': 200,
}

assento2 = {
    'pessoa': lista_pessoas[1],
    'numeracao': 2,
    'tipo': 'Leito',
    'custo': 200,
}

assento3 = {
    'pessoa': lista_pessoas[2],
    'numeracao': 3,
    'tipo': 'Semi-leito',
    'custo': 150,
}

assento4 = {
    'pessoa': lista_pessoas[3],
    'numeracao': 4,
    'tipo': 'Semi-leito',
    'custo': 150,
}

assento5 = {
    'pessoa': lista_pessoas[4],
    'tipo': 'Semi-leito',
    'numeracao': 5,
    'custo': 150,
}
lista_assentos = [assento1, assento2, assento3, assento4, assento5]


bilhete1 = {
    'pessoa': lista_assentos[0]['pessoa']['nome'],
    'assento': lista_assentos[0]['numeracao'],
    'tipo': lista_assentos[0]['tipo'],
    'data': '02/10/2023', 
    'horario': '11:00', 
    'origem': 'Curitiba',
    'destino': 'Rio de Janeiro',
}

bilhete2 = {
    'pessoa': lista_assentos[1]['pessoa']['nome'],
    'assento': lista_assentos[1]['numeracao'],
    'tipo': lista_assentos[1]['tipo'],
    'data': '02/10/2023', 
    'horario': '11:00', 
    'origem': 'Curitiba',
    'destino': 'Rio de Janeiro',
}

bilhete3 = {
    'pessoa': lista_assentos[2]['pessoa']['nome'],
    'assento': lista_assentos[2]['numeracao'],
    'tipo': lista_assentos[2]['tipo'],
    'data': '02/10/2023', 
    'horario': '11:00', 
    'origem': 'Curitiba',
    'destino': 'Rio de Janeiro',
}

bilhete4 = {
    'pessoa': lista_assentos[3]['pessoa']['nome'],
    'assento': lista_assentos[3]['numeracao'],
    'tipo': lista_assentos[3]['tipo'],
    'data': '02/10/2023', 
    'horario': '11:00', 
    'origem': 'Curitiba',
    'destino': 'Rio de Janeiro',
}

bilhete5 = {
    'pessoa': lista_assentos[4]['pessoa']['nome'],
    'assento': lista_assentos[4]['numeracao'],
    'tipo': lista_assentos[4]['tipo'],
    'data': '02/10/2023', 
    'horario': '11:00', 
    'origem': 'Curitiba',
    'destino': 'Rio de Janeiro',
}

lista_bilhetes = [bilhete1, bilhete2, bilhete3, bilhete4, bilhete5]

onibus = {
    'placa': 'ABC-123',
    'chassi': 'abgf456k7k',
    'documentacao': '123456asdfg',
    'bilhetes': lista_bilhetes
}