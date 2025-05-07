# YouTube to SharePoint

[🇧🇷 Versão em Português](README.pt.md)

Automate the process of embedding videos from a YouTube playlist directly into a SharePoint page.  
Ideal for internal teams who frequently publish video content in corporate portals.

## 🎯 What It Does

- Collects all videos from a public YouTube playlist.
- Requires manual login to Microsoft Office 365.
- Inserts YouTube video links into predefined SharePoint webparts.
- Publishes the updated SharePoint page.
- Supports a GUI for input; headless mode not yet implemented.

---

## 🖥️ Preview

> 📹 Fetch playlist → 🔐 Office login → 🧩 Auto-embed in SharePoint → ✅ Publish

---

## ⚙️ How to Use

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/AnaClaraSM/youtube-to-sharepoint.git
cd youtube-to-sharepoint
pip install -r requirements.txt
```

### 2. Run the Script

```bash
python main.py
```

You'll be prompted to paste:
- The YouTube Playlist URL
- The SharePoint page URL
- Office Login (when directed to the page)

---

## 💼 Requirements

- Python 3.8+
- Google Chrome or Edge installed
- ChromeDriver or EdgeDriver installed and in PATH
- SharePoint editing permissions
- Required Python packages:
  - selenium
  - customtkinter (future enhancements)

> ✅ Tested on Windows 10 and Chrome 122+

---

## 📂 Project Structure

```
📦 youtube-to-sharepoint
 ┣ 📁 automation
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
 ┣ 📄 README.md          ← Main (English)
 ┣ 📄 README.pt.md       ← Portuguese version
 ┗ 📄 requirements.txt
```

---

## ⚠️ Notes

- Ensure your SharePoint page has the **exact number** of YouTube webparts as the number of videos in the playlist (excluding the hidden ones).
- The script **does not create webparts**, only fills them.
- The login to Office 365 must be performed **manually in the browser window opened by the application**.
- Currently supports only **public** or **unlisted** YouTube playlists.

---

## 📜 License

MIT License
