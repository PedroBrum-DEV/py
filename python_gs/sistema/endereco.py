import requests  # Biblioteca para fazer requisições HTTP

class Endereco:
    def __init__(self, cep):
        # Ao criar uma instância, já busca os dados do endereço pelo CEP e armazena em self.dados
        self.dados = self.obter_endereco(cep)

    def obter_endereco(self, cep):
        # Monta a URL da API ViaCEP para buscar informações do CEP no formato JSON
        url = f"https://viacep.com.br/ws/{cep}/json/"
        # Faz uma requisição GET para a API ViaCEP
        resp = requests.get(url)
        # Verifica se a requisição foi bem-sucedida (código 200)
        if resp.status_code == 200:
            dados = resp.json()  # Converte a resposta JSON em dicionário Python
            # Verifica se não houve erro no retorno (ex: CEP inválido retorna um campo "erro")
            if not dados.get("erro"):
                return dados  # Retorna os dados do endereço
        # Se não obteve sucesso ou o CEP for inválido, retorna None
        return None
