import requests

class Clima:
    def __init__(self, _=None):
        self.headers = {
            "User-Agent": "SeuApp/1.0 contact@example.com"  # personalize isso
        }

    def obter_geolocalizacao(self, endereco):
        url = f"https://nominatim.openstreetmap.org/search?q={endereco}&format=json&limit=1"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 200 and resp.json():
            dados = resp.json()[0]
            return float(dados["lat"]), float(dados["lon"])
        return None, None

    def obter_clima(self, lat, lon):
        url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 200:
            dados = resp.json()
            instante = dados["properties"]["timeseries"][0]
            detalhes = instante["data"]["instant"]["details"]
            temp = detalhes.get("air_temperature", 0)
            vento = detalhes.get("wind_speed", 0)
            chuva = dados["properties"]["timeseries"][0]["data"].get("next_1_hours", {}).get("details", {}).get("precipitation_amount", 0)
            return round(temp, 1), round(vento, 1), round(chuva, 1)
        return None, None, None