class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.divida = 0
        self.filmes_locados = []

    def alugar(self, filme):
        self.filmes_locados.append(filme) 
        self.divida += filme.get_preco()
    
    def pagar_divida(self, valor_pago):
        self.divida -= valor_pago 
