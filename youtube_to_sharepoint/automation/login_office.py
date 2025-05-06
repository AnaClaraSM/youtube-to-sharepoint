from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Importa o WebDriverWait para esperas dinâmicas
from selenium.webdriver.support import expected_conditions as EC
from config.variables import office_home_url, office_login_btn_id # Importa variáveis de urls e elementos para a automação


# LOGIN OFFICE

def login_office(driver):
    # Acessa o office
    driver.get("https://www.office.com/")

    # Busca o botão de login
    office_login_btn = driver.find_element(By.ID, office_login_btn_id)

    # Clica no botão
    driver.execute_script("arguments[0].click();", office_login_btn)

    # Define espera máxima do navegador para o login
    login_wait =  WebDriverWait(driver, 300) # 5min (300s)

    # Espera até que a página tenha sido redirecionada para o Office (login realizado)
    try:
        login_wait.until(EC.url_contains(office_home_url))
    # Se após 5 minutos o login não tiver sido realizado
    except:
        # Retorna mensagem de erro no terminal (em vermelho)
        print("\033[91mAUTOMAÇÃO INTERROMPIDA: Login não realizado.\033[0m")
        # Fecha o navegador
        driver.close()
        # Interrompe o programa
        exit()