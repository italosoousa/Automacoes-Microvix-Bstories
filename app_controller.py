from auto.login import realizar_login
from auto.selecionar_empresa import selecionar_empresa
from auto.acessar_relatorio import acessar_relatorio
from auto.gerar_relatorio import gerar_relatorios
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

def executar_login(numeroLoja):
    usuario = os.getenv("USUARIO")
    senha = os.getenv("SENHA")
    codigo_loja = numeroLoja
    data1 = "01/06/2025"
    data2 = "30/06/2025"

    navegador = realizar_login(usuario, senha)
    selecionar_empresa(navegador, codigo_loja)
    acessar_relatorio(navegador)
    gerar_relatorios(navegador, data1, data2, numeroLoja)
