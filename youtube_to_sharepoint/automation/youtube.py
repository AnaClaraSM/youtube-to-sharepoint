from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.variables import yt_playlist_video_selector

# YOUTUBE

def get_playlist_videos(driver, yt_playlist_url):
   
    # Navega até o link da playlist
    driver.get(yt_playlist_url)

    # Espera até que ao menos um vídeo esteja visível
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, yt_playlist_video_selector))
    )

    # Busca todos os vídeos da playlist pelo seu seletor css e armazena em uma lista
    videos = driver.find_elements(By.CSS_SELECTOR, yt_playlist_video_selector)
    print(f"{len(videos)} vídeos encontrados.")

    # Extrai os links (href) de cada vídeo e armazena em uma lista (list comprehension)
    href_playlist = [video.get_attribute("href") for video in videos]

    # Corrige os links da playlist, se necessário 
    url_playlist = [] #lista para urls completas 
    for video_href in href_playlist:
        # Se o link não começa com https...com
        if not video_href.startswith("https://www.youtube.com"):
            url_playlist.append(f"https://www.youtube.com{video_href}") # completa o link e adiciona
        # Senão
        else:
            url_playlist.append(video_href) # apenas adiciona o link
        # OBS.: Verificar possibilidade de outros casos

    return url_playlist