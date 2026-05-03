# 💰 Manajemen Keuangan Anak Kos

## 📌 Deskripsi

Aplikasi **Manajemen Keuangan Anak Kos** merupakan aplikasi berbasis GUI yang dikembangkan menggunakan **PySide6** dan **SQLite** untuk membantu pengguna dalam mencatat, mengelola, dan memantau pemasukan serta pengeluaran secara sederhana namun terstruktur.

Aplikasi ini dirancang khusus untuk mahasiswa atau anak kos agar dapat mengontrol kondisi keuangan secara lebih efektif melalui pencatatan transaksi harian.

---

## 🎯 Tujuan

* Membantu pengguna mencatat pemasukan dan pengeluaran
* Menyediakan informasi saldo secara otomatis
* Memberikan visualisasi sederhana terhadap kondisi keuangan
* Mengimplementasikan konsep pemrograman visual dan database

---

## ⚙️ Teknologi yang Digunakan

* **Python 3**
* **PySide6** (GUI Framework)
* **SQLite** (Database)
* **QSS (Qt Style Sheet)** untuk styling tampilan

---

## 🧩 Fitur Utama

* ✅ Input data transaksi (5 field):

  * Keterangan
  * Jumlah uang
  * Tipe (Pemasukan / Pengeluaran)
  * Kategori
  * Tanggal
* ✅ Penyimpanan data menggunakan SQLite (persisten)
* ✅ Tampilan data menggunakan QTableWidget
* ✅ Fitur Edit dan Hapus data
* ✅ Fitur pencarian (search)
* ✅ Fitur filter (Semua / Pemasukan / Pengeluaran)
* ✅ Perhitungan saldo otomatis (running balance)
* ✅ Visualisasi warna:

  * Hijau → Pemasukan
  * Merah → Pengeluaran
* ✅ Menu bar (File & Bantuan)
* ✅ Status bar menampilkan Nama dan NIM
* ✅ Styling menggunakan file QSS eksternal

---

## 🏗️ Struktur Project (Separation of Concerns)

```
finance_app/
│
├── main.py              # Entry point aplikasi
├── main_window.py      # UI utama & logika aplikasi
├── dialog_finance.py   # Form input (dialog)
├── database.py         # Manajemen database SQLite
├── config.py           # Konfigurasi nama & NIM
└── style.qss           # Styling tampilan
```

---

## 🧠 Konsep yang Digunakan

* **Event-Driven Programming** (signals & slots)
* **Separation of Concerns (SoC)**
* **CRUD Database (Create, Read, Update, Delete)**
* **Running Balance Algorithm** untuk menghitung saldo
* **UI/UX sederhana berbasis warna**

---

## 🔢 Cara Kerja Fitur Saldo

Saldo dihitung secara otomatis menggunakan metode **running balance**, yaitu:

* Jika transaksi adalah **pemasukan**, maka:

  ```
  saldo += jumlah
  ```
* Jika transaksi adalah **pengeluaran**, maka:

  ```
  saldo -= jumlah
  ```

Perhitungan ini dilakukan pada fungsi `load_data()` di file `main_window.py`, sehingga saldo selalu ter-update setiap kali data berubah.

---

## 🚀 Cara Menjalankan Aplikasi

1. Install dependency:

   ```
   pip install PySide6
   ```

2. Jalankan aplikasi:

   ```
   python main.py
   ```

---

## 📷 Tampilan Aplikasi

(Silakan tambahkan screenshot di sini)

---

## 👤 Identitas Pengembang

* **Nama:** [Isi Nama Kamu]
* **NIM:** [Isi NIM Kamu]

---

## 📄 Catatan

Aplikasi ini dibuat sebagai bagian dari tugas mini project mata kuliah **Pemrograman Visual**, dengan fokus pada implementasi GUI, database, dan arsitektur program yang terstruktur.

---

## 📌 Kesimpulan

Aplikasi ini berhasil mengintegrasikan antarmuka GUI, database SQLite, serta logika pemrosesan data dalam satu sistem yang utuh. Dengan fitur yang tersedia, aplikasi ini dapat membantu pengguna dalam mengelola keuangan secara sederhana, efektif, dan informatif.
