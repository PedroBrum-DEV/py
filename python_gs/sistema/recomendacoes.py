class Recomendacoes:
    def __init__(self):
        # Dicionário com tipos de desastres naturais e suas recomendações divididas em três fases:
        # "antes" (prevenção), "durante" (ação durante o desastre) e "depois" (recuperação)
        self.tipos = {
            "inundacao": {
                "antes": [
                    "Evite construir em áreas sujeitas a enchentes.",
                    "Tenha rotas de fuga definidas.",
                    "Mantenha documentos importantes em local elevado e protegido."
                ],
                "durante": [
                    "Desligue a energia elétrica.",
                    "Evacue imediatamente se a água estiver subindo.",
                    "Evite contato com a água da enchente — pode estar contaminada."
                ],
                "depois": [
                    "Evite retorno imediato; aguarde autorização das autoridades.",
                    "Desinfete superfícies contaminadas pela água.",
                    "Documente prejuízos para eventual indenização."
                ]
            },
            # Mesma estrutura para outros tipos de desastres...
            "alagamento": {
                "antes": [
                    "Não descarte lixo em ruas e bueiros.",
                    "Limpe calhas e sistemas de drenagem com frequência."
                ],
                "durante": [
                    "Evite passar por ruas alagadas, mesmo com carro.",
                    "Busque abrigo em locais altos e seguros."
                ],
                "depois": [
                    "Verifique se há rachaduras ou danos estruturais no imóvel.",
                    "Lave roupas e objetos atingidos com água e sabão."
                ]
            },
            "deslizamento": {
                "antes": [
                    "Evite construções em encostas e áreas instáveis.",
                    "Fique atento a rachaduras em paredes e muros.",
                    "Plante vegetação para ajudar na contenção do solo."
                ],
                "durante": [
                    "Abandone imediatamente o local em caso de sinais de deslizamento.",
                    "Procure abrigo em áreas seguras e altas."
                ],
                "depois": [
                    "Evite retornar sem autorização de engenheiros ou Defesa Civil.",
                    "Reforce encostas com barreiras e drenagem adequada."
                ]
            },
            "ventos fortes": {
                "antes": [
                    "Reforce telhados e estruturas vulneráveis.",
                    "Retire objetos soltos de áreas externas."
                ],
                "durante": [
                    "Mantenha-se longe de janelas e portas de vidro.",
                    "Evite sair de casa durante rajadas fortes."
                ],
                "depois": [
                    "Verifique danos estruturais antes de usar energia elétrica.",
                    "Comunique danos à Defesa Civil." 
                ]
            },
            "ciclone": {
                "antes": [
                    "Tenha suprimentos essenciais para pelo menos 3 dias.",
                    "Feche portas e janelas com segurança."
                ],
                "durante": [
                    "Fique em um cômodo seguro, longe de janelas.",
                    "Desligue gás e eletricidade se recomendado."
                ],
                "depois": [
                    "Evite áreas alagadas e cabos elétricos caídos.",
                    "Ajude vizinhos em necessidade, se possível." 
                ]
            },
            "seca": {
                "antes": [
                    "Armazene água de maneira segura.",
                    "Utilize técnicas de irrigação eficientes."
                ],
                "durante": [
                    "Evite desperdício de água em todas as atividades.",
                    "Proteja plantações e criações com sombra e água."
                ],
                "depois": [
                    "Aproveite chuvas para recarregar reservatórios.",
                    "Revise o uso consciente da água na comunidade." 
                ]
            },
            "queimada": {
                "antes": [
                    "Evite uso de fogo em vegetação seca.",
                    "Mantenha terrenos limpos e com aceiros."
                ],
                "durante": [
                    "Cubra nariz e boca com pano úmido ao respirar.",
                    "Afaste-se da direção da fumaça."
                ],
                "depois": [
                    "Evite contato com a área queimada até resfriar.",
                    "Reporte o ocorrido a autoridades ambientais." 
                ]
            },
            "terremoto": {
                "antes": [
                    "Fixe prateleiras e móveis pesados nas paredes.",
                    "Tenha kit de emergência e rotas de evacuação."
                ],
                "durante": [
                    "Proteja-se embaixo de mesas fortes ou batentes.",
                    "Afaste-se de janelas, espelhos e objetos que possam cair."
                ],
                "depois": [
                    "Evacue com calma e evite elevadores.",
                    "Cuidado com vazamentos de gás e fios elétricos." 
                ]
            }
        }

    def obter(self, tipo):
        # Recebe o tipo de desastre e retorna as recomendações formatadas para as três fases
        info = self.tipos.get(tipo)
        if not info:
            return "Tipo de desastre não reconhecido."
        
        # Monta uma string organizada com as recomendações para antes, durante e depois do desastre
        return (
            f"🟡 ANTES:\n" + "\n".join(f"• {x}" for x in info["antes"]) +
            f"\n\n🔴 DURANTE:\n" + "\n".join(f"• {x}" for x in info["durante"]) +
            f"\n\n🟢 DEPOIS:\n" + "\n".join(f"• {x}" for x in info["depois"])
        )
