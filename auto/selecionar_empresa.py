from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import time

def selecionar_empresa(navegador: WebDriver, empresa_index: int):
    espera = WebDriverWait(navegador, 20)

    try:
        # Seleciona a empresa baseado no index

        time.sleep(2)
        empresa_XPATH = f'(//a[@class="company-link"])[{empresa_index}]'
        espera.until(EC.element_to_be_clickable((By.XPATH, empresa_XPATH))).click()

        time.sleep(15)

        print("🏢 Empresa selecionada com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao selecionar empresa: {e}")

        