from .endereco import Endereco
from .clima import Clima
from .recomendacoes import Recomendacoes

def analisar_desastres_por_cep(cep):
    # 1. Obter endereço
    endereco = Endereco(cep)

    if not endereco.dados:
        print("❌ CEP inválido ou não encontrado.")
        return

    cidade = endereco.dados.get("localidade")
    uf = endereco.dados.get("uf")
    endereco_completo = f"{cidade}, {uf}"

    print(f"📍 Local: {endereco_completo}")

    # 2. Obter clima
    clima_api = Clima("834129b2fd0d445784c140119253005")
    lat, lon = clima_api.obter_geolocalizacao(endereco_completo)
    if lat is None or lon is None:
        print("❌ Não foi possível obter geolocalização.")
        return

    temp_c, vento_kph, chuva_mm = clima_api.obter_clima(lat, lon)
    print(f"🌡️ Temperatura: {temp_c}°C")
    print(f"💨 Ventos: {vento_kph} km/h")
    print(f"🌧️ Chuva: {chuva_mm} mm")

    # 3. Analisar risco
    tipo_desastre = None
    if vento_kph >= 90:
        tipo_desastre = "ciclones"
    elif vento_kph >= 60:
        tipo_desastre = "ventos fortes"
    elif chuva_mm >= 60:
        tipo_desastre = "inundacoes"
    elif chuva_mm >= 30:
        tipo_desastre = "alagamento"

    if tipo_desastre:
        print(f"⚠️ Possível risco de: {tipo_desastre.upper()}")
        recomendacao = Recomendacoes().obter(tipo_desastre)
        print(f"📢 Recomendação: {recomendacao}")
    else:
        print("✅ Sem risco de desastre natural detectado.")

