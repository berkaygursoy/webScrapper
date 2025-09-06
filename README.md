# Headline Scraper

Modern web scraping tool that extracts headlines from HaberTürk's homepage and exports them to an Excel file.

## Features

- ✅ Dynamic HTML parsing with BeautifulSoup
- ✅ Error handling for network issues and website structure changes
- ✅ Clear output formatting in console and Excel
- ✅ Uses proper HTTP headers to mimic legitimate browser traffic
- ✅ Tracks source and timestamps data
- 📊 Well-formatted Excel export compatible with modern spreadsheet applications

## Installation & Requirements

To use this script, you'll need:

1. Python 3.7+
2. Required libraries:
   - requests (`pip install requests`)
   - beautifulsoup4 (`pip install beautifulsoup4`)
   - pandas (`pip install pandas`)

Install all dependencies with:
```bash
pip install requests beautifulsoup4 pandas openpyxl


## Usage

Save the code in a file named haberturk_scraper.py
Run the script from command line:
python haberturk_scraper.py
The scraped headlines will be saved to an Excel file named haberturk_headlines.xlsx](https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/License-MIT-green
https://img.shields.io/badge/Status-Active-brightgreen

Bu proje, web sayfalarından veri çekip Excel formatında kaydeden Python tabanlı bir uygulamadır.

📋 Proje Açıklaması
Python'un requests, BeautifulSoup ve pandas kütüphanelerini kullanarak web sayfalarından veri çeken ve bu verileri Excel formatında kaydeden bir script.

🚀 Özellikler
🌐 Web sayfalarından HTTP istekleri ile içerik çekme

🧹 BeautifulSoup ile HTML içeriğini ayrıştırma

📊 Pandas ile veri işleme ve düzenleme

💾 Excel formatında veri kaydetme

⚡ Hızlı ve etkili veri işleme

📦 Kurulum

Gereksinimler
Python 3.8+
pip (Python paket yöneticisi)

🛠️ Kullanım

Temel Kullanım

python scraper.py
Özelleştirme
Kodu farklı web siteleri için özelleştirmek için aşağıdaki değişkenleri düzenleyebilirsiniz:

python
# URL'yi değiştirin
url = "https://hedef-site.com/"

# Farklı HTML elementleri kullanın
basliks = soup.find_all("h1")  # veya "h2", "h3", "div", etc.

# Farklı çıktı formatları
df.to_csv("sonuclar.csv", index=False)  # CSV formatında kaydetme

📁 Dosya Yapısı

web-scraping-project/
│
├── scraper.py                 # Ana scraping scripti
├── requirements.txt           # Bağımlılıklar
├── example_basliklar.xlsx     # Örnek çıktı dosyası
├── README.md                  # Bu dosya
└── .gitignore                 # Git ignore dosyası

📝 Örnek Çıktı

Çalıştırma sonrasında aşağıdaki gibi bir çıktı alacaksınız:
Haber başlıkları 'example_basliklar.xlsx' dosyasına kaydedildi.
Oluşturulan Excel dosyası şu şekilde görünecektir:

Başlıklar

İlk haber başlığı
İkinci haber başlığı
Üçüncü haber başlığı
🔧 Geliştirme

Bağımlılıklar

Proje şu kütüphanelere bağlıdır:

requests - HTTP istekleri için

beautifulsoup4 - HTML ayrıştırma için

pandas - Veri işleme için

openpyxl - Excel çıktıları için
