from auto.login import realizar_login
from auto.selecionar_empresa import selecionar_empresa
from auto.acessar_relatorio import acessar_relatorio
from auto.gerar_relatorio import gerar_relatorios

def executar_login(numeroLoja):
    usuario = "italo.meca"
    senha = "@86Kizzmacca7"
    codigo_loja = numeroLoja
    data1 = "01/06/2025"
    data2 = "05/06/2025"

    navegador = realizar_login(usuario, senha)
    selecionar_empresa(navegador, codigo_loja)
    acessar_relatorio(navegador)
    gerar_relatorios(navegador, data1, data2, numeroLoja)