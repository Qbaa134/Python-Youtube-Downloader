import yt_dlp

def display_available_streams(url):
    try:
        # Opcje do pobrania dostępnych strumieni
        ydl_opts = {
            'quiet': True,
            'format': 'best',  # Domyślnie wybieramy najlepszy format
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Pobieramy informacje o wideo
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])

            # Wyświetlamy dostępne rozdzielczości i formaty
            print("\nDostępne opcje wideo:")
            for idx, f in enumerate(formats):
                if f.get('vcodec') != 'none':  # Sprawdzamy, czy jest to strumień wideo
                    print(f"{idx + 1}. Rozdzielczość: {f.get('height')}p, Format: {f.get('ext')}, FPS: {f.get('fps')}")

            return formats

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None

def download_video(url, audio_only=False, selected_format=None):
    try:
        # Opcje pobierania wideo lub audio
        ydl_opts = {
            'format': selected_format if selected_format else 'best',  # Wybór formatu
            'noplaylist': True,  # Pobieramy tylko jedno wideo
            'outtmpl': '%(title)s.%(ext)s',  # Określenie nazwy pliku
        }

        if audio_only:
            # Jeśli tylko audio, ustawiamy format na bestaudio
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegAudioConvertor',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Pobieranie wideo lub audio
            ydl.download([url])

        print("Pobieranie zakończone!")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    url = input("Podaj URL wideo z YouTube: ")
    option = input("Wybierz opcję (1: wideo, 2: audio MP3): ")

    if option == "1":
        # Wyświetlamy dostępne rozdzielczości
        formats = display_available_streams(url)

        if formats:
            choice = int(input("\nWybierz numer opcji wideo: ")) - 1
            selected_format = formats[choice].get('format_id')
            download_video(url, audio_only=False, selected_format=selected_format)
    elif option == "2":
        download_video(url, audio_only=True)
    else:
        print("Niepoprawny wybór!")
