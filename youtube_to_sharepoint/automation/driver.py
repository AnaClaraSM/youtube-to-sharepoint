from selenium import webdriver # Importa o WebDriver para acesso ao navegador

# NAVEGADOR

# Inicia o navegador
def start_driver():
    # Instancia e inicializa o Navegador
    driver = webdriver.Chrome()
    # Maximiza a tela do navegador
    driver.maximize_window()

    return driver