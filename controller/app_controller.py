from auto.login import realizar_login
from auto.selecionar_empresa import selecionar_empresa
from auto.acessar_relatorio import acessar_relatorio

def executar_login(numeroLoja):
    usuario = "italo.meca"
    senha = "@86Kizzmacca7"
    codigo_loja = numeroLoja

    navegador = realizar_login(usuario, senha)
    selecionar_empresa(navegador, codigo_loja)
    acessar_relatorio(navegador)