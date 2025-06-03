import requests
 
class Clima:
    def __init__(self, chave_api):
        self.chave = chave_api
 
    def obter_geolocalizacao(self, endereco):
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={endereco}&limit=1&appid={self.chave}"
        resp = requests.get(url)
        if resp.status_code == 200 and resp.json():
            dados = resp.json()[0]
            return dados["lat"], dados["lon"]
        return None, None
 
    def obter_clima(self, lat, lon):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.chave}&units=metric"
        resp = requests.get(url)
        if resp.status_code == 200:
            dados = resp.json()
            temp = dados["main"]["temp"]
            vento = dados["wind"]["speed"] * 3.6  # m/s para km/h
            chuva = dados.get("rain", {}).get("1h", 0)
            return round(temp, 1), round(vento, 1), round(chuva, 1)
        return None, None, None