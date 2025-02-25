Oto przykładowy plik `README.md` dla tego projektu:


# YouTube Video & Audio Downloader

Prosty skrypt Python do pobierania filmów i audio z YouTube za pomocą biblioteki `yt-dlp`.

## 📋 Wymagania

- Python 3.7+
- `yt-dlp`
- `ffmpeg` (do konwersji audio na MP3)

## ⚙️ Instalacja

1. Zainstaluj `yt-dlp` i `ffmpeg`:

```bash
pip install yt-dlp
```

W systemie Linux możesz zainstalować `ffmpeg` za pomocą:

```bash
sudo apt update && sudo apt install ffmpeg
```

Na Windowsie możesz pobrać `ffmpeg` ze strony: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## 🚀 Użycie

1. Uruchom skrypt:

```bash
python downloader.py
```

2. Podaj link do wideo z YouTube i wybierz opcję:

- **1:** Pobieranie wideo (z możliwością wyboru rozdzielczości).
- **2:** Pobieranie samego audio w formacie MP3.

3. Skrypt pobierze wybrany plik i zapisze go w bieżącym katalogu.

## 🛠️ Przykład działania

### Pobieranie wideo:

```
Podaj URL wideo z YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Wybierz opcję (1: wideo, 2: audio MP3): 1

Dostępne opcje wideo:
1. Rozdzielczość: 1080p, Format: mp4, FPS: 30
2. Rozdzielczość: 720p, Format: mp4, FPS: 30

Wybierz numer opcji wideo: 1

Pobieranie zakończone!
```

### Pobieranie audio:

```
Podaj URL wideo z YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Wybierz opcję (1: wideo, 2: audio MP3): 2

Pobieranie zakończone!
```

## 📄 Struktura projektu

```
.
├── downloader.py   # Główny skrypt
└── README.md       # Dokumentacja
```

## ❗ Uwagi

- Skrypt obsługuje tylko pojedyncze filmy (playlisty są pomijane).
- Do pobierania MP3 wymagany jest `ffmpeg`.

## 📝 Licencja

Ten projekt jest udostępniony na licencji MIT.

## 🤝 Wsparcie

Jeśli masz pytania lub problemy, otwórz issue na GitHubie!
