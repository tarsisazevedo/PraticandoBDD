class Locadora:
    def __init__(self):
        self.clientes = []
        self.filmes = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def get_clientes(self):
        return self.clientes

    def get_filmes(self):
        return self.filmes

    def cadastrar_filme(self, filme):
        self.filmes.append(filme)
