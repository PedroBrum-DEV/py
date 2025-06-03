from sistema.desastres import analisar_desastres_por_cep
from sistema.clima import Clima
from sistema.endereco import Endereco
from sistema.recomendacoes import Recomendacoes

def menu():
    clima_api = Clima()  # Instancia a classe Clima para usar as funções de previsão meteorológica

    while True:
        # Menu principal apresentado para o usuário
        print("""
=== Menu Interativo ===
1- Ver previsão local (por CEP)
2- Recomendações de segurança
3- Como posso fazer parte de projetos sociais
4- Como posso receber doações
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Opção para consultar a previsão do tempo por CEP
            cep = input("Digite o CEP: ")
            endereco = Endereco(cep)  # Busca os dados do endereço via CEP

            if endereco.dados:
                # Monta uma string com endereço completo para consulta
                completo = f"{endereco.dados.get('logradouro', '')}, {endereco.dados.get('bairro', '')}, {endereco.dados.get('localidade', '')}, {endereco.dados.get('uf', '')}"
                print(f"Consultando previsão para: {completo}")

                # Obtém latitude e longitude do endereço completo
                lat, lon = clima_api.obter_geolocalizacao(completo)

                if lat and lon:
                    # Consulta o clima para a localização obtida
                    temp, vento, chuva = clima_api.obter_clima(lat, lon)
                    if temp is not None:
                        # Exibe os dados climáticos formatados
                        print(f"\n🌤️ Clima em {completo}:\n🌡️ Temperatura: {temp}°C\n💨 Vento: {vento} m/s\n🌧️ Chuva: {chuva} mm")
                    else:
                        print("❌ Não foi possível obter dados climáticos.")
                else:
                    print("❌ Não foi possível obter geolocalização.")
            else:
                print("❌ CEP inválido ou não encontrado.")

        elif opcao == "2":
            # Opção para mostrar recomendações de segurança baseadas no tipo de desastre informado
            tipo = input("Digite o tipo de desastre: ").lower()  # Entrada do tipo de desastre em minúsculas
            recomendador = Recomendacoes()  # Instancia a classe de recomendações
            print(f"📢 {recomendador.obter(tipo)}")  # Exibe as recomendações para o tipo informado

        elif opcao == "3":
            # Opção para informar como o usuário pode participar de projetos sociais
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
            else:
                print("❌ Opção inválida.")

        elif opcao == "4":
            # Opção para informar como receber doações
            print("📦 Procure ONGs ou grupos de apoio locais. Centros de referência social (CRAS) também podem ajudar.")

        else:
            # Caso o usuário digite uma opção inválida no menu principal
            print("❌ Opção inválida.")

        # Pergunta se o usuário quer voltar ao menu principal
        continuar = input("Deseja voltar ao menu? (s/n): ")
        if continuar.lower() != 's':
            print("👋 Encerrando...")
            break

menu()  # Chama a função menu para iniciar o programa
