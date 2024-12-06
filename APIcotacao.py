import requests

principais_moedas = ["USD", "EUR", "GBP", "JPY", "BRL", "AUD", "CAD", "CNY"]

moeda1 = input("Digite uma moeda(ex: BRL, USD, EUR, GBP, AUD, CAD, JPY, CNY): ").upper()

# requisição de cada moeda da lista de principais moedas
for moeda2 in principais_moedas:
    if moeda1 != moeda2:  # comparação para que não haja moedas iguais
        par = moeda1 + moeda2 # cocatenação
        try:
            # requisição da API
            cotacoes = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda1}-{moeda2}")
            cotacoes.raise_for_status()  # verifica se houve algum erro na requisição
            cotacoes = cotacoes.json() 
            
            # extrai a cotação
            if par in cotacoes:
                cotacao = cotacoes[par]["bid"]
                print(f"A cotação de {moeda1} para {moeda2} é: {cotacao}")
            else:
                print(f"Não foi possível encontrar a cotação para {moeda1}-{moeda2}.")
        except requests.exceptions.RequestException as e: # erros de requisição http
            print(f"Erro ao acessar a API de {moeda1}-{moeda2}: {e}")