class Recomendacoes:
    def __init__(self):
        self.tipos = {
            "ciclones": "Fique em casa, mantenha portas e janelas fechadas. Evite áreas abertas.",
            "ventos fortes": "Afaste-se de janelas e áreas com risco de queda de objetos.",
            "inundacoes": "Evacue áreas de risco e evite contato com a água contaminada.",
            "alagamento": "Não tente atravessar ruas alagadas, desligue equipamentos elétricos."
        }
 
    def obter(self, tipo):
        return self.tipos.get(tipo, "Tipo de desastre não reconhecido.")