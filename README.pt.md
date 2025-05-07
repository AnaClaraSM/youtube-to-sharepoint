# YouTube to SharePoint

[🇺🇸 English Version](README.md)

Automatize o processo de incorporação de vídeos de uma playlist do YouTube diretamente em uma página do SharePoint.
Ideal para equipes internas que frequentemente publicam conteúdo de vídeo em portais corporativos.

## 🎯 O que ele faz

* Coleta todos os vídeos de uma playlist pública do YouTube.
* Requer login manual no Microsoft Office 365.
* Insere os links dos vídeos do YouTube em webparts pré-definidos no SharePoint.
* Publica a página do SharePoint atualizada.
* Suporta uma interface gráfica para input; o modo headless ainda não foi implementado.

---

## 🖥️ Visualização

> 📹 Buscar playlist → 🔐 Login no Office → 🧩 Incorporação automática no SharePoint → ✅ Publicação

---

## ⚙️ Como usar

### 1. Clonar e instalar dependências

```bash
git clone https://github.com/seu-usuario/youtube-to-sharepoint.git
cd youtube-to-sharepoint
pip install -r requirements.txt
```

### 2. Rodar o script

```bash
python main.py
```

Será solicitado que você insira:

* A URL da Playlist do YouTube
* A URL da página do SharePoint

---

## 💼 Requisitos

* Python 3.8+
* Google Chrome ou Edge instalados
* ChromeDriver ou EdgeDriver instalados e no PATH
* Permissões de edição no SharePoint
* Pacotes Python necessários:

  * selenium
  * customtkinter (melhorias futuras)

> ✅ Testado no Windows 10 e Chrome 122+

---

## 📂 Estrutura do Projeto

```
📦 youtube-to-sharepoint
 ┣ 📁 automacao
 ┃ ┣ 📄 driver.py
 ┃ ┣ 📄 login_office.py
 ┃ ┣ 📄 youtube.py
 ┃ ┣ 📄 sharepoint.py
 ┃ ┗ 📄 utils.py
 ┣ 📁 config/
 ┃ ┗ 📄 variables.py
 ┣ 📄 inputs.py
 ┣ 📄 main.py
 ┣ 📄 LICENSE
 ┣ 📄 README.md          ← Versão Principal (Inglês)
 ┣ 📄 README.pt.md       ← Versão em Português
 ┗ 📄 requirements.txt
```

---

## ⚠️ Notas

* Certifique-se de que a página do SharePoint tenha o **número exato** de webparts do YouTube, de acordo com o número de vídeos na playlist (excluindo os ocultos).
* O script **não cria webparts**, ele apenas preenche-os.
* O login no Office 365 deve ser feito **manualmente na janela do navegador aberta pelo aplicativo**.
* Atualmente, suporta apenas playlists do YouTube **públicas** ou **não listadas**.

---

## 📜 Licença

Licença MIT