# 🤖 BORRY - CHATBOT RRI
Chatbot sederhana yang dibangun menggunakan algoritma Naive Bayes untuk memproses percakapan, serta menggunakan framework Flask untuk diintegrasikan ke dalam aplikasi web.

## 💡 FITUR
- Chatbot dengan algoritma Naive Bayes.
- Web interface menggunakan Flask.
- Antarmuka berbasis HTML dan CSS (template & static).
- Dataset chatbot yang bisa dikembangkan.

## ▶️ Cara Menjalankan Proyek
### Clone Repository
```
git clone https://github.com/namapengguna/borry_chatbot_rri.git
cd borry_chatbot_rri
```

### Aktifkan Virtual Environment
Buat virtual environment
```
python -m venv venv
```
Aktifkan:
- Windows:
```
venv\Scripts\activate
```
- Linux/macOS:
```
source venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Jalankan Aplikasi
```
python app.py
```

## 🧠 TECH
- **Naive Bayes Classifier :**
Digunakan untuk mengklasifikasi maksud (intent) dari input pengguna berdasarkan dataset yang disediakan. Model dilatih lalu disimpan sebagai file .pkl (model_chatbot.pkl).
- **Flask Web Framework :**
Menyediakan antarmuka web agar pengguna dapat berinteraksi dengan chatbot melalui browser.

