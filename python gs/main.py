import sistema as si
from sistema import analisar_desastres_por_cep

from .sistema import Clima
from .sistema import Endereco
from .sistema import Recomendacoes
 
def menu():
    clima_api = si.Clima("834129b2f0d0445784c140119253005")
 
    while True:
        print("""
=== Menu Interativo ===
1- Ver previsão local (por CEP)
2- Recomendações de segurança
3- Como posso fazer parte de projetos sociais
4- Como posso receber doações
""")
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            cep = input("Digite o CEP: ")
            endereco = si.Endereco(cep)
            if endereco.dados:
                completo = f"{endereco.dados.get('logradouro', '')}, {endereco.dados.get('bairro', '')}, {endereco.dados.get('localidade', '')}, {endereco.dados.get('uf', '')}"
                print(f"Consultando previsão para: {completo}")
                lat, lon = clima_api.obter_geolocalizacao(completo)
                if lat and lon:
                    temp, vento, chuva = clima_api.obter_clima(lat, lon)
                    print(f"\n🌤️ Clima em {completo}:\n🌡️ Temperatura: {temp}°C\n💨 Vento: {vento} km/h\n🌧️ Chuva: {chuva} mm")
        elif opcao == "2":
            tipo = input("Digite o tipo de desastre: ").lower()
            recomendador = si.Recomendacoes()
            print(f"📢 {recomendador.obter(tipo)}")
        elif opcao == "3":
            print("""
1 - Voluntário
2 - Doação financeira
3 - Doação de materiais
""")
            sub = input("Escolha: ")
            if sub == "1":
                print("💙 Seja voluntário em ONGs locais que atuam na sua região.")
            elif sub == "2":
                print("💸 Faça doações em sites confiáveis como Vakinha, Benfeitoria ou diretamente em ONGs.")
            elif sub == "3":
                print("🎁 Doe alimentos, roupas, itens de higiene para centros de apoio ou igrejas próximas.")
        elif opcao == "4":
            print("📦 Procure ONGs ou grupos de apoio locais. Centros de referência social (CRAS) também podem ajudar.")
        else:
            print("❌ Opção inválida.")
 
        continuar = input("Deseja voltar ao menu? (s/n): ")
        if continuar.lower() != 's':
            print("👋 Encerrando...")
            break
 
menu()
 
 