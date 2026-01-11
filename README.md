# Prof Akademi - Flask Web Uygulaması

Minimalist ve düzenli yapılı Flask web uygulaması.

## Kurulum & Çalıştırma

```bash
# Sanal ortam oluştur
python -m venv venv

# Etkinleştir
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Bağımlılıkları yükle
pip install -r requirements.txt

# Başlat
python app.py
```

Uygulama: `http://localhost:5000`

## Proje Yapısı

```
prof_akademi/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/fonts.css
    ├── fonts/
    └── images/
```

## Stack

- **Framework**: Flask 3.0.0
- **CSS**: Tailwind CSS (CDN)
- **Font**: MADE TOMMY
