#encoding: utf-8

from pyhistorian import *
from should_dsl import *

from cliente import *
from locadora import *

class CadastrandoClientes(Historia):
    """
    Como um dono da locadora
    Eu quero cadastrar meus clientes
    Para que ele possa alugar muitos filmes
    """

    colored = True

class CadastrarCliente(Cenario):
    @DadoQue("eu sou um cliente que quer se cadastrar na locadora")
    def sou_um_cliente_que_quer_se_cadastrar(self):
        self.cliente = Cliente("Tarsis")
        self.locadora = Locadora()

    @Quando("o adimistrador pega meus dados")
    def pegar_os_dados_do_cliente(self):
        self.locadora.inserir_cliente(self.cliente)

    @Entao("eu estou cadastrado e posso pegar filmes")
    def verificar_o_cliente_cadastrado(self):
        self.locadora.get_clientes() |should_have| self.cliente

class CadastrarDoisClientes(Cenario):
    DadoQue("eu sou um cliente que quer se cadastrar na locadora")
    @DadoQue("eu sou outro cliente que quer se cadastrar na locadora")
    def sou_outro_cliente_que_quer_se_cadastrar(self):
        self.outro_cliente = Cliente("Tarsis 2")

    Quando("o adimistrador pega meus dados")
    @Quando('o adminstrador pega os dados do outro cliente')
    def pegar_dados_do_outro_cliente(self):
        self.locadora.inserir_cliente(self.outro_cliente)

    Entao("eu estou cadastrado e posso pegar filmes")
    @Entao("o outro cliente tambem está cadastrado")
    def verificar_se_o_outro_cliente_esta_cadastrado(self):
        self.locadora.get_clientes() |should_have| self.outro_cliente

if __name__=='__main__':
    CadastrandoClientes.run()
 
