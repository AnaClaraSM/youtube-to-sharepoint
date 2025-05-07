import customtkinter as ctk
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode # Biblioteca para tratamento de url 

# Função

def get_user_urls2():
    
    # Solicita os links ao usuário
    yt_playlist_url = entry_youtube.get()
    sp_page_url = entry_sharepoint.get()

    # Valida os campos
    if (yt_playlist_url != "") and (sp_page_url != ""):

        label_validacao.configure(text="URLs validados. Iniciando automação...", text_color="green")
        
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

        # Fecha a janela
        app.destroy()

        # Retorna os links da playlist e da página editável
        return yt_playlist_url, sp_page_edit_url
    else:
        label_validacao.configure(text="Você precisa preencher os dois campos.", text_color="red")
        

# Configuração da aparência
ctk.set_appearance_mode('light') # system (default), light, dark

# Criação da janela principal
app = ctk.CTk()
app.title('YouTube To Sharepoint') # Título
app.geometry("400x250") # Tamanho

# Criação dos campos

# Espaçamento superior

top_spacer = ctk.CTkFrame(app, height=10, fg_color="transparent")
top_spacer.pack()

# Label -> ctk.CTkLabel(janela, text=texto)
label_youtube = ctk.CTkLabel(app, text="Playlist do YouTube") # Cria o campo
label_youtube.pack(pady=(10,3)) # Adiciona o campo na aplicação

# Entry -> ctk.CTkEntry(janela, placeholder_text=texto)
entry_youtube = ctk.CTkEntry(app, placeholder_text="Insira o URL da playlist do YouTube", width=250)
entry_youtube.pack(pady=(3,10))

# Label
label_sharepoint = ctk.CTkLabel(app, text="Página do Sharepoint")
label_sharepoint.pack(pady=(10,3))

# Entry
entry_sharepoint = ctk.CTkEntry(app, placeholder_text="Insira o URL da página do Sharepoint", width=250)
entry_sharepoint.pack(pady=(3,10))

# Botão
button_iniciar = ctk.CTkButton(app, text="Iniciar", command=get_user_urls2)
button_iniciar.pack(pady=(15,10))

# Label
label_validacao = ctk.CTkLabel(app, text="")
label_validacao.pack()



# Obtem as dimensões da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

# Define as dimensões da janela
largura_janela = 400
altura_janela = 280

# Calcula a posição para centralizar
x = (largura_tela // 2) - (largura_janela // 2)
y = (altura_tela // 2) - (altura_janela // 2)

# Atualiza a geometria com a posição
app.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")



# Mantém a janela aberta
app.mainloop()