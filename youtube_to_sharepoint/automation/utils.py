from selenium.webdriver.common.by import By
import time # Biblioteca de tempo

# FUNÇÕES


# ROLAR PÁGINA

def scroll_page(driver, scroll_pause_time = 2):
# Recebe como parâmetros o navegador (driver) e o intervalo entre rolagens (2s por padrão)

    # Variáveis de rolagem
    screen_height = driver.execute_script("return window.innerHeight;") # altura de tela
    scroll_height = driver.execute_script("return document.body.scrollHeight;") # altura total da página (quanto a página pode ser rolada)
    current_position = 0 # posição atual

    # Loop
    while current_position < scroll_height:
        driver.execute_script("window.scrollBy(0, arguments[0]);", screen_height) # Rola a seção para baixo pela altura da tela - (X=0 , Y=screen_height) 
        time.sleep(scroll_pause_time) # aguarda o intervalo
        current_position += screen_height # atualiza a posição atual, somando a altura da tela
        scroll_height = driver.execute_script("return document.body.scrollHeight;") # atualiza altura total (restante) da página
    # Aguarda 2s
    time.sleep(scroll_pause_time)
    # Rola de volta para o topo
    driver.execute_script("window.scrollTo(0, 0);")
    # Aguarda mais 2s
    time.sleep(scroll_pause_time)

# ROLAR PÁGINA SHAREPOINT

def scroll_section(driver, scrollable_section_selector, scroll_pause_time = 2):
# Recebe como parâmetros o navegador (driver), a seção rolável e o intervalo entre rolagens (2s por padrão)

    # Obtém o elemento rolável
    scrollable_element = driver.find_element(By.CSS_SELECTOR, scrollable_section_selector)
    
    # Variáveis de rolagem
    screen_height = driver.execute_script("return arguments[0].clientHeight;", scrollable_element) # altura de tela (da seção rolável)
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element) # altura total da página/seção rolável (quanto a página pode ser rolada)
    current_position = 0 # posição atual

    # Loop
    while current_position < scroll_height:
        driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scrollable_element, screen_height) # Rola a seção para baixo pela altura da tela - (X=0 , Y=screen_height) 
        time.sleep(scroll_pause_time) # aguarda o intervalo
        current_position += screen_height # atualiza a posição atual, somando a altura da tela
        scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element) # atualiza altura total (restante) da página
    # Aguarda 2s
    time.sleep(scroll_pause_time)
    # Rola de volta para o topo
    driver.execute_script("arguments[0].scrollTo(0, 0);", scrollable_element)
    # Aguarda mais 2s
    time.sleep(scroll_pause_time)