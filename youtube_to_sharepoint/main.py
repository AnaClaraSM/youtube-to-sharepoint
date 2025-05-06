from automation.driver import start_driver
from automation.login_office import login_office
from automation.youtube import get_playlist_videos
from automation.sharepoint import add_videos_sharepoint
from inputs import get_user_urls


def main():
    # ENTRADAS DE USUÁRIO
    yt_playlist_url, sp_page_edit_url = get_user_urls()

    # 1. NAVEGADOR
    driver = start_driver()

    # 2. LOGIN OFFICE
    login_office(driver)

    # 3. YOUTUBE
    url_playlist = get_playlist_videos(driver, yt_playlist_url)

    # 4. SHAREPOINT
    add_videos_sharepoint(driver, sp_page_edit_url, url_playlist)

    # 5. FECHAR O NAVEGADOR
    driver.quit()

# Execução
if __name__ == "__main__":
    main()