from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import time


def acessar_relatorio(navegador: WebDriver):
    espera = WebDriverWait(navegador, 20)

    try:
        # Selecionando o Icone de faturamento para chegar no relatório
        lupa = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lupaBuscaMenu"]/a')))
        lupa.click()

        # Coloca o nome do relaotório na barra de pesquisa
        caixaBusca = espera.until(EC.element_to_be_clickable((By.ID, 'caixaBuscaModal')))
        caixaBusca.send_keys("Produtos/Serv.Vendidos")

        # Clica no relatório encontrado
        relatorio = espera.until(EC.element_to_be_clickable((By.ID, 'linkBuscaMenu_0')))
        relatorio.click()

        time.sleep(5)


        print("📄 Acesso ao relatório realizado com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao acessar relatório: {e}")

        