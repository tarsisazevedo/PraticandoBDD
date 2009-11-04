from filme import *
from locadora import *

from pyhistorian import *
from should_dsl import should_have

class CadastrarFilmes(Historia):
    """
    Como um administrador da locadora
    Eu quero cadastrar filmes
    Para que os meus clientes tenham o que alugar
    """
    cenarios = ['CadastrandoUmFilme', 'CadastrandoDoisFilmes']
    colored = True

class CadastrandoUmFilme(Cenario):
    @DadoQue("Eu sou o administrador da locadora")
    def criar_locadora(self):
        self.locadora = Locadora()

    @Quando("Eu cadastro um filme do Batman")
    def cadastrar_um_filme_do_batman(self):
        self.filme_do_batman = Filme('Batman', 4.50)
        self.locadora.cadastrar_filme(self.filme_do_batman)

    @Entao("Minha locadora tem um filme do batman para ser alugado")
    def minha_locadora_tem_um_filme_cadastrado(self):
        self.locadora.get_filmes() |should_have| self.filme_do_batman

class CadastrandoDoisFilmes(Cenario):
    DadoQue('Eu sou o administrador da locadora')
    
    Quando('Eu cadastro um filme do Batman')
    @Quando('eu cadastro um filme do superman')
    def cadastrar_um_filme_do_superman(self):
        self.filme_do_superman = Filme('Superman', 4.00)
        self.locadora.cadastrar_filme(self.filme_do_superman)
    
    Entao('Minha locadora tem um filme do batman para ser alugado')
    @Entao('minha locadora tem um filme do superman para ser alugado')
    def minha_locadora_tem_um_filme_do_superman_para_ser_alugado(self):
        self.locadora.get_filmes() |should_have| self.filme_do_superman

CadastrarFilmes.run()
