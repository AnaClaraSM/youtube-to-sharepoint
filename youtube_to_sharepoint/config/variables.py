# ELEMENTOS PARA A AUTOMAÇÃO

# OFFICE

# URL Office 365 - Home
office_home_url = "https://m365.cloud.microsoft/?auth=2"

# Botão de login
office_login_btn_id = "hero-banner-sign-in-microsoft-365-link"


# YOUTUBE

# Link da Playlist de Vídeos -> solicitada ao usuário

# Seletor de Vídeo Individual da Playlist (Tag a)
yt_playlist_video_selector = "a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer"


# SHAREPOINT

# Página do Sharepoint -> solicitada ao usuário

# Seletor da seção rolável da página
sp_scrollable_section_selector = "[data-automation-id=\"contentScrollRegion\"]"

# Seletor do campo de inserção de link do Youtube (div)
sp_video_url_field_selector = "textarea[placeholder*='https://www.youtube.com']"

# Classe dos botões de adicionar vídeo e atualizar notícias
sp_primary_button_class = "ms-Button--primary"

# Seletor da thumbnail de vídeo do youtube adicionado
sp_video_thumbnail_selector = "iframe[src*='youtube.com/embed']"