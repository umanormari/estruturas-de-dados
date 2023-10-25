from datetime import datetime # Importe o módulo datetime para trabalhar com datas

ano_admissao = int(input('Qual foi o ano de sua admissão? ')) # Obtenha o ano de admissão como uma entrada do usuário
ano_atual = datetime.now().year # Obtenha o ano atual

for ano in range(ano_admissao, ano_atual + 1):
    ano_limite = ano + 1 # Calcule o ano limite para as férias
    if ano_limite <= ano_atual: # Verifique se o ano limite é menor ou igual ao ano atual # Se for menor ou igual, as férias podem ser tiradas no mesmo mês do ano limite
        mes_limite = 12  # Dezembro é o mês 12
    else: # Se for maior, as férias devem ser tiradas em dezembro do ano anterior ao limite
        mes_limite = 12  # Dezembro é o mês 12, independentemente do ano
    print(f'Para o ano {ano}, suas férias precisarão ocorrer até: {mes_limite:02d}/{ano_limite}')
