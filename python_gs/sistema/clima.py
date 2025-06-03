import requests  # Biblioteca para fazer requisições HTTP

class Clima:
    def __init__(self, _=None):
        # Define um cabeçalho para as requisições HTTP, identificando o aplicativo para os serviços externos
        self.headers = {
            "User-Agent": "SeuApp/1.0 contact@example.com"  # personalize com seu app e contato
        }

    def obter_geolocalizacao(self, endereco):
        # Monta a URL da API do OpenStreetMap para buscar coordenadas geográficas pelo endereço
        url = f"https://nominatim.openstreetmap.org/search?q={endereco}&format=json&limit=1"
        # Faz uma requisição GET para a API, enviando os headers
        resp = requests.get(url, headers=self.headers)
        # Verifica se a resposta foi bem-sucedida (status 200) e se há dados retornados
        if resp.status_code == 200 and resp.json():
            dados = resp.json()[0]  # Pega o primeiro resultado do JSON retornado
            # Retorna latitude e longitude convertidos para float
            return float(dados["lat"]), float(dados["lon"])
        # Caso não encontre dados, retorna None para lat e lon
        return None, None

    def obter_clima(self, lat, lon):
        # Monta a URL da API de clima do MET Norway com latitude e longitude
        url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
        # Faz uma requisição GET para a API, enviando os headers
        resp = requests.get(url, headers=self.headers)
        # Verifica se a resposta foi bem-sucedida (status 200)
        if resp.status_code == 200:
            dados = resp.json()  # Parseia o JSON retornado
            instante = dados["properties"]["timeseries"][0]  # Pega o primeiro instante de tempo (previsão mais recente)
            detalhes = instante["data"]["instant"]["details"]  # Detalhes instantâneos do clima
            temp = detalhes.get("air_temperature", 0)  # Temperatura do ar (°C)
            vento = detalhes.get("wind_speed", 0)     # Velocidade do vento (m/s)
            # Quantidade de precipitação prevista para a próxima 1 hora, se disponível
            chuva = dados["properties"]["timeseries"][0]["data"].get("next_1_hours", {}).get("details", {}).get("precipitation_amount", 0)
            # Retorna temperatura, vento e chuva arredondados com 1 casa decimal
            return round(temp, 1), round(vento, 1), round(chuva, 1)
        # Caso não consiga obter os dados do clima, retorna None para cada valor
        return None, None, None
