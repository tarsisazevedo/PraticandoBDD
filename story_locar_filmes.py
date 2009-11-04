#encoding: utf-8
 
from pyhistorian import *
from should_dsl import *

from cliente import Cliente
from filme import Filme

class LocarUmFilme(Historia):
    """
    Como um usuario registrado na locadora 
    Eu quero locar um filme 
    Para que eu leve o filme pra minha casa
    """
    cenarios = ['LocandoUmFilme', 'LocandoDoisFilmes', 'LocandoDoisFilmesPagandoSoUm', 'LocandoDoisFilmesPagandoOsDois']
    colorido=True
    

class LocandoUmFilme(Cenario):
    @DadoQue('Eu estou na locadora e quero alugar um filme do Batman')
    def quero_alugar_um_filme_do_batman(self):
        self.filme_do_batman = Filme("Batman", 4.50)
        self.cliente = Cliente("eu")

    @Quando('eu alugo o filme do batman no valor de 4.50')
    def alugar_o_filme_do_batman(self):
        self.cliente.alugar(self.filme_do_batman)

    @Entao('eu tenho uma divida de 4.50 com a locadora')
    def estou_devendo_4_e_50(self):
        self.cliente.divida |should_be.equal_to| 4.50

    @Entao("eu levo o filme pra casa")
    def terminar_a_locacao_do_filme_do_batman(self):
        self.cliente.filmes_locados |should_have| self.filme_do_batman

class LocandoDoisFilmes(Cenario):
    @DadoQue("Eu estou na locadora e quero alugar um filme do batman e outro do superman")
    def quero_alugar_dois_filmes(self):
        self.cliente = Cliente("eu")
        self.filme_do_batman = Filme("Batman", 4.50)
        self.filme_do_superman = Filme("Super Man", 4.00)

    @Quando("eu alugo o filme do batman, com o preço de 4.50, e do superman, com o preço de 4.00")
    def alugar_os_dois_filmes(self):
        self.cliente.alugar(self.filme_do_batman)
        self.cliente.alugar(self.filme_do_superman)
        
    @Entao("eu tenho uma divida de 8.50 com a locadora")
    def estou_devendo_7_e_50(self):
        self.cliente.divida |should_be.equal_to| 8.50

    @Entao("eu levo os 2 filmes para casa")
    def terminar_a_locacao_dos_dois_filmes(self):
        self.cliente.filmes_locados |should_have| self.filme_do_batman, self.filme_do_superman


class LocandoDoisFilmesPagandoSoUm(Cenario):
    @DadoQue("Eu estou na locadora para pagar a divida do aluguel de 2 filmes no valor de 8.50")
    def divida_do_aluguel_de_dois_filmes(self):
        self.cliente = Cliente("eu")
        self.filme_do_batman = Filme("Batman", 4.50)
        self.filme_do_superman = Filme("Super Man", 4.00)
        self.cliente.alugar(self.filme_do_batman)
        self.cliente.alugar(self.filme_do_superman)
        self.cliente.divida |should_be.equal_to| 8.50

    @Quando('eu pago 4.00')
    def pagar_parte_da_divida(self):
        self.cliente.pagar_divida(4.00)

    @Entao('eu tenho uma divida de 4.50 com a locadora')
    def divida_por_pagar(self):
        self.cliente.divida |should_be.equal_to| 4.50       

class LocandoDoisFilmesPagandoOsDois(Cenario):
    DadoQue("Eu estou na locadora para pagar a divida do aluguel de 2 filmes no valor de 8.50")
    
    @Quando('eu pago toda a $divida', '8.50')
    def pagar_toda_a_divida(self, divida):
        self.cliente.pagar_divida(float(divida))

    @Entao('eu nao tenho mais divida com a locadora')
    def divida_zerada(self):
        self.cliente.divida |should_be.equal_to| 0

if __name__=='__main__':
    LocarUmFilme.run()
