from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Importa o WebDriverWait para esperas dinâmicas
from selenium.webdriver.support import expected_conditions as EC
import time # Biblioteca de tempo
from config.variables import sp_scrollable_section_selector, sp_primary_button_class, sp_video_url_field_selector, sp_video_thumbnail_selector
from automation.utils import scroll_section

# SHAREPOINT

def add_videos_sharepoint(driver, sp_page_edit_url, url_playlist):

    # OBS.: O layout da página onde estarão os cursos deve estar previamente definido. Deve conter todas as youtube webparts necessárias, conforme o número de vídeos da playlist.

    # Navega até a página do Sharepoint em Modo de Edição
    driver.get(sp_page_edit_url)

    # Aguarda o carregamento da página e do modo de edição
    time.sleep(5) # 5s

    # Buscar botões da página

    # Rola a página para garantir o carregamento de todos os botões
    scroll_section(driver, sp_scrollable_section_selector, 1) # Função de rolagem

    add_video_buttons = [] # Cria lista para botões de adicionar vídeo

    # Busca todos os botões primários (adicionar vídeo e atualizar página)
    primary_buttons = driver.find_elements(By.CLASS_NAME, sp_primary_button_class)

    # Filtra os botões
    for button in primary_buttons:
        # Se o texto do botão contiver "Adicionar Vídeo"
        if "Adicionar vídeo" in button.text:
            # Adiciona o botão à lista específica
            add_video_buttons.append(button)
        # Se o texto for "Atualizar notícias (página)"
        elif "Atualizar notícias" or "Republicar" in button.text:
            # Armazena o botão
            update_page_button = button


    # Valida se o número de vídeos corresponde ao número de botões e se o botão de atualizar foi encontrado
    if (len(url_playlist) != len(add_video_buttons)) or (not update_page_button):
        if len(url_playlist) != len(add_video_buttons):
            print("\033[91mERRO: Número de vídeos não corresponde ao número de botões para adição de vídeo.\033[0m")
            print(f"Vídeos encontrados: {len(url_playlist)}")
            print(f"Botões encontrados: {len(add_video_buttons)}")
        elif not update_page_button:
            print("\033[91mERRO: Botão de atualizar não encontrado.\033[0m")
            print(f"Botão de atualizar: {update_page_button}")
        driver.close()
        exit()
        
    # Se total de botões Adicionar vídeo < total de vídeos OU se !update_page_button -> REALIZA A ROLAGEM, BUSCA E FILTRAGEM NOVAMENTE, com intervalo igual a intervalo+1 (demora mais para rolar); Por mais uma tentativa (tentativa = 1; tentativa <= 2; tentativa +=1;). Se erro. Fechar execução e retornar erro de webparts insuficientes.

    # Para cada botão de adicionar vídeo (enumerando os índices)
    for index, add_button in enumerate(add_video_buttons):
        # Rola até que o botão esteja visível
        driver.execute_script("arguments[0].scrollIntoView();", add_button)
        # Aguarda a visibilidade do botão ou até 10s
        WebDriverWait(driver, 10).until(EC.visibility_of(add_button))
        # Clica no botão de adicionar vídeo (utiliza JS para contornar a sobreposição de divs ao botão)
        # Se for o primeiro botão, clica duas vezes
        if index == 0:
            driver.execute_script("arguments[0].click();", add_button)
            time.sleep(2) # Aguarda 2s
            driver.execute_script("arguments[0].click();", add_button)
        # Para os próximos, clica apenas uma vez
        else:
            driver.execute_script("arguments[0].click();", add_button)
        time.sleep(2) # Aguarda 2s a visbilidade do campo de link
        # Busca o campo de inserção de link pelo seletor
        url_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sp_video_url_field_selector)))
        url_field = driver.find_element(By.CSS_SELECTOR, sp_video_url_field_selector)
        # Digita o link correspondente ao índice do botão
        url_field.send_keys(url_playlist[index])
        # Aguarda até que a thumbnail fique visível ou até 3 minutos
        WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.CSS_SELECTOR, sp_video_thumbnail_selector)))
        # Aguarda mais 1 segundos (para garantir carregamento)
        time.sleep(1)
        time.sleep(5) # espera mais 5 segundos para carregar completamente

    # Atualiza a página
    # Rola até botão de atualizar ficar visível
    driver.execute_script("arguments[0].scrollIntoView();", update_page_button)
    # Aguarda a visibilidade do botão ou até 10s
    WebDriverWait(driver, 10).until(EC.visibility_of(update_page_button))
    # Clica no botão
    driver.execute_script("arguments[0].click();", update_page_button)

    # Aguarda 10s
    time.sleep(10)