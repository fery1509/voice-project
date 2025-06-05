import speech_recognition as sr  # Untuk pengenalan suara
import subprocess  # Untuk menjalankan perintah sistem
import pyttsx3  # Untuk AI suara offline
import os  # Untuk membuka aplikasi sistem

# Inisialisasi AI Suara
engine = pyttsx3.init()

# Mengatur suara AI ke suara wanita
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():  # Sesuaikan dengan nama suara wanita yang tersedia
        engine.setProperty('voice', voice.id)
        break  # Gunakan suara wanita pertama yang ditemukan

def speak(text):
    """Mengucapkan teks dengan suara AI."""
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    """Mendengarkan perintah tanpa wake word."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Silakan ucapkan perintah...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-US")
        print("Anda mengucapkan:", command)
        return command.lower()
    
    except sr.UnknownValueError:
        print("Maaf, saya tidak mengenali suara Anda.")
        speak("Maaf, saya tidak mengenali suara Anda.")
    except sr.RequestError:
        print("Kesalahan jaringan. Periksa koneksi internet Anda.")
        speak("Kesalahan jaringan. Periksa koneksi internet Anda.")
    
    return ""

def execute_command(command):
    """Menjalankan perintah berdasarkan input suara pengguna."""
    if "open command prompt" in command:
        print("Membuka Command Prompt...")
        speak("Membuka Command Prompt")
        subprocess.Popen("cmd")

    elif "open calculator" in command:
        print("Membuka Kalkulator...")
        speak("Membuka Kalkulator")
        subprocess.Popen("calc")

    elif "open chrome" in command:
        print("Membuka Google Chrome...")
        speak("Membuka Google Chrome")
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "open whatsapp" in command:
        print("Membuka WhatsApp Desktop...")
        speak("Membuka WhatsApp Desktop")
        subprocess.Popen("C:\\Users\\MyBook Hype AMD\\AppData\\Local\\WhatsApp.exe")

    elif "open visual studio code" in command:
        print("Membuka Visual Studio Code...")
        speak("Membuka Visual Studio Code")
        subprocess.Popen("C:\\Users\\MyBook Hype AMD\\AppData\\Local\\Programs\\Microsoft VS Code\\_\\Code.exe")

    else:
        print("Perintah tidak dikenali.")
        speak("Maaf, saya tidak mengerti perintah itu. Silakan coba lagi.")
        return False  # Tandai perintah gagal

    return True  # Tandai perintah berhasil

def main():
    # AI menyambut saat program dijalankan
    speak("Selamat datang Master Fery, ada yang bisa saya bantu hari ini?")
    
    while True:  # Program akan terus berjalan hingga ditutup
        command = listen_for_command()  # Dengarkan perintah langsung
        if command:
            execute_command(command)  # Jalankan perintah

if __name__ == "__main__":
    main()
