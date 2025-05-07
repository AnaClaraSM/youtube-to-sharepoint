from tkinter import *
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode # Biblioteca para tratamento de url 

# ENTRADAS DE USUÁRIO COM INTERFACE GRÁFICA

# Coleta os links (playlist do youtube e página do sharepoint) informados pelo usuário
def get_user_urls():

    # Cria a janela
    window = Tk()
    # window.withdraw() # Esconde a janela principal (mostrando apenas as de diálogo)

    # Título da janela
    window.title("YouTube To Sharepoint Automation")

    # Rótulo
    label = Label(window, text="Rótulo 1!")
    label.pack()

    window.mainloop()
    
    # Solicita os links ao usuário
    # yt_playlist_url = simpledialog.askstring("Playlist do Youtube", "Digite o link da playlist do YouTube: ")
    # sp_page_url = simpledialog.askstring("Página do Sharepoint", "Digite o link da página do SharePoint: ")

    # Trata o link do sharepoint para estar em modo de edição

    # Converte a url de str para objeto
    parsed = urlparse(sp_page_url)
    # Transforma a query do objeto em um dicionário
    query = parse_qs(parsed.query)
    # Garante que o modo seja de edição
    query["Mode"] = ["Edit"]
    # Reconstrói a query string
    new_query = urlencode(query, doseq=True)
    # Reconstrói a url completa, com a nova query
    sp_page_edit_url = urlunparse(parsed._replace(query=new_query))

    # Retorna os links da playlist e da página editável
    return yt_playlist_url, sp_page_edit_url

get_user_urls()