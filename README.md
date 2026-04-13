# Tugas Praktikum Sistem Pakar: Diagnosa PC (GUI)

File ini berisi program untuk tugas Praktikum Sistem Pakar tingkat dasar. Program ini dibuat menggunakan bahasa Python dengan tampilan antarmuka grafis (GUI) dari library bawaan Tkinter.

## Deskripsi Program
Aplikasi ini adalah program sederhana yang berfungsi untuk mendiagnosa 5 jenis kerusakan perangkat atau sistem berdasarkan input gejala yang dicentang oleh pengguna:
1. Motherboard Bermasalah / Baterai CMOS Lemah
2. Baterai Laptop Drop Parah
3. Keyboard Konslet / Rusak
4. Infeksi Virus / Ransomware pada Sistem Operasi
5. Kabel Fleksibel Layar Terputus

## Penjelasan Kode & Logika
Sesuai dengan instruksi dari tugas, program ini benar-benar tidak menggunakan logika bertingkat if-else panjang. Logika utamanya disusun menggunakan pendekatan struktur data:

1. **Knowledge Base (Dictionary):**
   Setiap data untuk nama kerusakan, syarat list gejala, dan solusinya dibungkus ke dalam satu list dictionary yang rapi bernama `aturan_diagnosa`.
2. **Mesin Inferensi (Fungsi Subset):**
   Untuk mendeteksi atau mencocokkan apakah gejala dari user sesuai dengan satu penyakit, program menggunakan pustaka Himpunan (Sets) bawaan Python yakni fungsi `.issubset()`. Fungsi ini akan mengecek otomatis apakah semua centangan pengguna memenuhi syarat validasi tanpa perlu menggunakan coding yang berjejer panjang.

## Cara Menjalankan Program

1. Buka Terminal atau Command Prompt.
2. Pindah atau arahkan (cd) ke letak direktori/folder penyimpan file ini.
3. Jalankan file python utama dengan perintah berikut ini:
   ```bash
   python sistem_pakar.py
   ```
4. Jendela utama dari aplikasi program akan langsung terbuka. Anda tinggal mencentang beberapa gejala lalu klik tombol proses untuk memunculkan notifikasi hasil akhirnya.

## Detail Blok Kode

- `aturan_diagnosa` : Logika dasar yang berperan sebagai penampung parameter database.
- `daftar_pertanyaan_gejala` : Berfungsi sebagai penerjemah kode referensi database menjadi kalimat bahasa Indonesia yang lebih santai untuk dibaca pengguna di layar.
- `class ProgramDiagnosaPC` : Tempat untuk mengatur ukuran jendela, perulangan (looping) checkbox, warna latar, tipe huruf utama, maupun scroll layar.
- `def eksekusi_diagnosa` : Aksi yang merespon klik tombol utama. Bertugas melempar data yang dicentang menuju proses himpunan matematika untuk dikomparasi dan segera mengeluarkan popup hasilnya.
