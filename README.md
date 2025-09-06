# 🕸️ **Web Scraper** – Python ile Web Veri Çekme

> “Basit bir script ile web sitelerinden veri çıkarıp Excel’e dönüştürün.”  
> Version: **1.0.0**

[![GitHub stars](https://img.shields.io/github/stars/berkaygursoy/webScrapper?style=social)](https://github.com/berkaygursoy/webScrapper/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/berkaygursoy/webScrapper?style=social)](https://github.com/berkaygursoy/webScrapper/network/members)

---

## 📖 Proje Açıklaması

Python, **BeautifulSoup** ve **Pandas** kullanarak bir web sayfasından veri çekip bu veriyi Excel dosyasına kaydeden minimalist bir kütüphane.  
Başlıklar, ürün listeleri veya herhangi bir HTML içeriği hızlıca çıkarılabilir.

---

## ✨ Öne Çıkan Özellikler

| # | Özellik | Açıklama |
|---|---------|----------|
| 1️⃣ | **Hızlı Scraping** | Tek satır kodla veri çekme. |
| 2️⃣ | **Excel Dışa Aktarımı** | Pandas ile `.xlsx` dosyası oluşturma. |
| 3️⃣ | **Esnek Seçiciler** | `tag`, `class`, `id` gibi seçimler desteklenir. |
| 4️⃣ | **Hata Yönetimi** | Otomatik yeniden deneme ve zaman aşımı ayarı. |

---

## ⚙️ Hızlı Kurulum

```bash
# 1. Depoyu klonla
git clone https://github.com/berkaygursoy/webScrapper.git
cd webScrapper

# 2. Sanal ortam oluştur (isteğe bağlı)
python -m venv .venv && source .venv/bin/activate   # Linux/Mac
# veya
.\.venv\Scripts\activate                          # Windows

# 3. Gerekli paketleri yükle
pip install -r requirements.txt

# 4. Çalıştır
python scraper.py

```
# Web Scraper Project

A lightweight Python script that scrapes headline titles from a website and stores them in an Excel file.  
It demonstrates the power of **requests**, **BeautifulSoup**, and **pandas** for quick data extraction and export.

---

## 📌 Overview

- **Purpose:** Pull article headlines (or any other text) from a given URL and save them as an `.xlsx` spreadsheet.
- **Use‑case:** News aggregation, content monitoring, research data collection, etc.
- **Why it matters:** No heavy frameworks needed—just three popular libraries.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Simple HTTP Requests** | Uses `requests` to fetch page content. |
| **HTML Parsing** | BeautifulSoup parses the DOM and extracts `<span>` tags (customizable). |
| **DataFrame Creation** | Pandas converts the list of titles into a structured DataFrame. |
| **Excel Export** | `to_excel()` writes data to an Excel file (`openpyxl` handles the format). |
| **Modular Code** | Easily replace tag names, attributes, or output paths. |

---

## 🛠️ Technologies

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- pandas
- openpyxl (dependency of `pandas.to_excel`)

---

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your‑username>/web-scraper.git
   cd web-scraper
2. **Create a virtual environment (recommended)**
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .\.venv\Scripts\activate
