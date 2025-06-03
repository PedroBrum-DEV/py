import requests
 
class Endereco:
    def __init__(self, cep):
        self.dados = self.obter_endereco(cep)
 
    def obter_endereco(self, cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resp = requests.get(url)
        if resp.status_code == 200:
            dados = resp.json()
            if not dados.get("erro"):
                return dados
        return None