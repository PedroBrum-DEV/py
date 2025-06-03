from .endereco import Endereco   # Importa a classe Endereco para buscar dados do CEP
from .clima import Clima         # Importa a classe Clima para obter informações climáticas
from .recomendacoes import Recomendacoes  # Importa a classe Recomendacoes para obter dicas

def analisar_desastres_por_cep(cep):
    # 1. Obter endereço a partir do CEP
    endereco = Endereco(cep)

    # Verifica se os dados do endereço foram obtidos com sucesso
    if not endereco.dados:
        print("❌ CEP inválido ou não encontrado.")
        return

    # Extrai cidade e estado (UF) dos dados do endereço
    cidade = endereco.dados.get("localidade")
    uf = endereco.dados.get("uf")
    endereco_completo = f"{cidade}, {uf}"  # Formata o endereço para consulta

    print(f"📍 Local: {endereco_completo}")

    # 2. Obter dados climáticos para o endereço
    clima_api = Clima("834129b2fd0d445784c140119253005")  # Instancia a API de clima (aparentemente a chave não está usada no código passado)
    lat, lon = clima_api.obter_geolocalizacao(endereco_completo)  # Busca latitude e longitude do local

    # Verifica se conseguiu obter a geolocalização
    if lat is None or lon is None:
        print("❌ Não foi possível obter geolocalização.")
        return

    # Obtém temperatura, velocidade do vento e precipitação em mm
    temp_c, vento_kph, chuva_mm = clima_api.obter_clima(lat, lon)
    print(f"🌡️ Temperatura: {temp_c}°C")
    print(f"💨 Ventos: {vento_kph} km/h")
    print(f"🌧️ Chuva: {chuva_mm} mm")

    # 3. Analisar o risco de desastres naturais com base nos dados climáticos
    tipo_desastre = None
    if vento_kph >= 90:
        tipo_desastre = "ciclones"        # Ventos muito fortes indicam ciclones
    elif vento_kph >= 60:
        tipo_desastre = "ventos fortes"   # Ventos fortes em menor intensidade
    elif chuva_mm >= 60:
        tipo_desastre = "inundacoes"      # Chuva intensa que pode causar enchentes
    elif chuva_mm >= 30:
        tipo_desastre = "alagamento"      # Chuva moderada que pode causar alagamentos

    # Caso haja algum risco identificado, exibe alerta e recomendação
    if tipo_desastre:
        print(f"⚠️ Possível risco de: {tipo_desastre.upper()}")
        recomendacao = Recomendacoes().obter(tipo_desastre)  # Busca a recomendação associada ao tipo de desastre
        print(f"📢 Recomendação: {recomendacao}")
    else:
        # Caso contrário, indica que não há risco
        print("✅ Sem risco de desastre natural detectado.")
