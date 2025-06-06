# 📝 Tentang Project
Project ini adalah sebuah asisten suara sederhana berbasis Python yang dibuat untuk mempermudah pengguna dalam menjalankan aplikasi di komputer hanya dengan perintah suara.

# 🎙️ Voice Assistant with Python

Sebuah **asisten suara sederhana berbasis Python** yang mampu mendengarkan perintah pengguna dan menjalankan aplikasi secara otomatis melalui pengenalan suara dan text-to-speech (TTS).

---

## 🧠 Fitur Utama

- 🎧 Mendengarkan perintah suara pengguna menggunakan Google Speech Recognition
- 🗣️ Menjawab dan memberikan feedback dengan suara AI wanita (offline TTS)
- ⚙️ Menjalankan aplikasi desktop seperti:
  - Command Prompt
  - Kalkulator
  - Google Chrome
  - WhatsApp Desktop
  - Visual Studio Code

---

## 🔧 Teknologi & Library

- `speech_recognition` – Untuk menangkap dan mengenali input suara pengguna
- `pyttsx3` – Untuk text-to-speech secara offline (tanpa internet)
- `subprocess` – Untuk mengeksekusi aplikasi Windows
- `os` – Untuk operasi file dan sistem

---

## 🚀 Cara Menjalankan Project

### 1. Install Library yang Dibutuhkan
Gunakan `pip` untuk menginstall semua dependensi:

```bash
pip install SpeechRecognition pyttsx3
python voice_assistant.py
