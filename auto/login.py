from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def realizar_login(usuario, senha) -> webdriver.Chrome:
    
    # Caminho da pasta de downloads no projeto
    caminho_downloads = os.path.join(os.getcwd(), "downloads")
    os.makedirs(caminho_downloads, exist_ok=True)

    # Configuração do Chrome com redirecionamento de downloads
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": caminho_downloads,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")
    navegador = webdriver.Chrome(options=options)
    espera = WebDriverWait(navegador, 20)


    try:
        # Acessar a página no navegador
        navegador.get("https://erp.microvix.com.br/")

        # Acha o elemento de login e digita o login
        espera.until(EC.presence_of_element_located((By.ID, "f_login"))).send_keys(usuario)

        # Achar o elemento de senha e digita a senha
        navegador.find_element(By.ID, "f_senha").send_keys(senha)

        # Seleciona o botão de entrar para confirmar
        navegador.find_element(By.ID, 'lmxta-login-btn-autenticar').click()

        print("✅ Login realizado com sucesso!")
        return navegador

    except Exception as e:
        print(f"❌ Erro ao fazer login: {e}")
        navegador.quit()  # Fecha só em caso de erro
        return None
   