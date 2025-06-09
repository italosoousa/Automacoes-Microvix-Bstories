from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def gerar_relatorios(navegador: WebDriver, data_inicial, data_final):
    espera = WebDriverWait(navegador, 20)

    visoes = [
    "COTY",
    "EXCELLENCE",
    "JUNO",
    "LOREAL",
    "LVMH",
    "PRESTIGE",
    "PUIG",
    "SHISEIDO",
    "SMART BEAUTY",
    "TFS",
    "VIZCAYA",
    "WEITNAUER"
    ]

    try:
        for visao in visoes:
            # Navegando até o iframe que está o relatório
            iframe = espera.until(EC.presence_of_element_located((By.ID, "main")))
            navegador.switch_to.frame(iframe)

            # Selecionando o relatório que está salvo na visão
            select_element = espera.until(EC.presence_of_element_located((By.ID, 'Form1_id_visao')))
            seletor = Select(select_element)
            seletor.select_by_visible_text(visao)

            # Gera o relatório
            botao_gerarRelatorio = espera.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Gerar Relatório"]')))
            botao_gerarRelatorio.click()

            # Preenchendo o campo das datas 
            for campo, valor in [("f_data1", data_inicial), ("f_data2", data_final)]:
                campo_data = espera.until(EC.element_to_be_clickable((By.ID, campo)))
                campo_data.click()
                campo_data.send_keys(Keys.CONTROL + "a")
                campo_data.send_keys(Keys.BACKSPACE)
                campo_data.send_keys(valor)

            botaoOK = espera.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ui-button-text-only")]')))
            botaoOK.click()

            # Sair do iframe e voltar ao conteúdo principal
            navegador.switch_to.default_content()

            # Entra no iframe para acessar o relatório
            iframe = espera.until(EC.presence_of_element_located((By.ID, "main")))
            navegador.switch_to.frame(iframe)

            # Clica no botão para gerar o relatório
            botaoExcel = espera.until(EC.element_to_be_clickable((By.ID, 'botaoExportarXLS')))
            botaoExcel.click()

            navegador.back()
            time.sleep(7)

            print(f"📥 Relatório da visão {visao} baixado com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao exportar Excel: {e}")