# 🚀 KASUZAZ Network Stresser (Python)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)

Alat simulasi ujian tekanan rangkaian (Layer 7 HTTP Flood) yang direka khas untuk tujuan pendidikan dan ujian keselamatan beretika. 

---

## 🛠️ Ciri-Ciri (Features)
* **Multithreading:** Mampu menghantar permintaan (requests) secara serentak untuk menguji beban pelayan.
* **User-Agent Spoofing:** Menukar header User-Agent secara rawak untuk meniru trafik manusia yang sebenar.
* **CLI Support:** Dibina untuk terminal (Kali Linux/Linux) menggunakan `argparse`.
* **Kredit:** Author by **kasuzaz**.

## 📖 Cara Penggunaan
Pastikan anda mempunyai Python 3 dipasang.

```bash
# Clone projek ini
git clone [https://github.com/KASUZAZ/ddos.python.git](https://github.com/KASUZAZ/ddos.python.git)

# Masuk ke folder
cd ddos.python

# Jalankan skrip (Contoh untuk IP Localhost)
python3 ddos.py -t 127.0.0.1 -p 80 -th 100
