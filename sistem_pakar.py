import tkinter as tk
from tkinter import messagebox, ttk

# Basis Pengetahuan / Aturan
aturan_diagnosa = {
    "Indikasi Motherboard Bermasalah / Penurunan Kualitas Baterai CMOS": {
        "gejala": {"usb_mati", "waktu_selalu_reset", "gagal_post_bios"},
        "solusi": "Periksa kondisi fisik motherboard. Ganti baterai CMOS (CR2032) dahulu. Hubungi teknisi perbaikan jalur kelistrikan mainboard."
    },
    "Indikasi Baterai Laptop Soak (Drop Parah)": {
        "gejala": {"mati_saat_cabut_charger", "tulisan_not_charging", "persentase_cepat_habis"},
        "solusi": "Sel baterai Anda rusak/kehabisan siklus. Selalu gunakan laptop dengan charger terpasang, atau beli baterai original."
    },
    "Indikasi Keyboard Konslet / Kerusakan Jalur Fleksibel Tuts": {
        "gejala": {"ngetik_sendiri", "tombol_tidak_merespon", "beep_saat_menyala"},
        "solusi": "Lumpuhkan fitur keyboard internal via Device Manager. Solusi terbaik adalah mengganti panel keyboard laptop secara utuh."
    },
    "Indikasi Infeksi Virus / Ransomware Fatal di Sistem Operasi": {
        "gejala": {"muncul_pop_up_aneh", "file_tidak_bisa_dibuka", "kinerja_100_persen_idle"},
        "solusi": "Lakukan Full Scan dengan Antivirus terupdate dan cabut internet. Jika file terenkripsi, segera Install ulang OS (Format)."
    },
    "Indikasi Kabel Fleksibel Layar / Kabel Ribbon Terputus": {
        "gejala": {"layar_kedip_saat_digerakkan", "tampil_di_monitor_eksternal", "warna_berubah_saat_ditekan"},
        "solusi": "LCD panel masih sangat sehat, namun sambungan kabel pita penghubung ke motherboard renggang/terjepit. Bawa ke service center."
    }
}

# Mapping Gejala ke Label Teks Pertanyaan
daftar_pertanyaan_gejala = {
    "usb_mati": "Apakah semua port luar (USB) mendadak tak merespon alias gagal membaca perangkat Flashdisk/Mouse?",
    "waktu_selalu_reset": "Apakah jam dan tanggal di Windows PC selalu otomatis terulang reset ke masa lampau bilamana dihidupkan?",
    "gagal_post_bios": "Apakah layar hanya terang samar, namun tidak kunjung memunculkan logo merk satupun & gagal masuk BIOS?",
    "mati_saat_cabut_charger": "Apakah mesin sistem laptop terputus otomatis/padam seketika di detik itu juga ketika ujung kabel charger dicabut?",
    "tulisan_not_charging": "Apakah jelas ditemukan teks 'Plugged in, not charging' (dicas, nge-stuck) di indikator persentase baterai Windows?",
    "persentase_cepat_habis": "Apakah sisa persenan indikator pengisian baterai terjun menukik drastis hingga angka mati hanya dalam hitungan sekian menit?",
    "ngetik_sendiri": "Apakah huruf/karakter terketik jalan berkelanjutan di kolom pengetikan text-box walaupun ujung jari tak menyentuh tuts satupun?",
    "tombol_tidak_merespon": "Apakah ditemui ada tuts/tombol grup spesifik di papan ketik yang tak memberikan output walau terus dipencet?",
    "beep_saat_menyala": "Apakah telinga mendengarkan lantunan rentetan nada dering peringatan (BEEP) bernada keras berpacu saat baru menekan Power?",
    "muncul_pop_up_aneh": "Apakah membludak berbagai macam tab/jendela asing maupun iklan situs antah-berantah yang tiba-tiba membajak layar penuh?",
    "file_tidak_bisa_dibuka": "Apakah berlimpah daftar dokumen (Word/Excel) yang berubah ekstensinya (.zzzzz) dan tak dapat lagi terbaca oleh sistem secara langsung?",
    "kinerja_100_persen_idle": "Apakah pandangan monitor utama lewat panel Task Manager menunjukkan grafik beban Processor memuncak 100% saat keadaan laptop tidak dipakai kegiatan apa-apa?",
    "layar_kedip_saat_digerakkan": "Apakah kalian merasakan timbulnya loncatan grafis/kedipan parah secara terang-terangan manakala engsel penutup monitor posisi buka tutup sering secara agresif digerakan pelan?",
    "tampil_di_monitor_eksternal": "Apakah status penampil utama seketika terpantau gelap gulita, namun dia sanggup dengan sempurna memancarkan cahaya layar pas dicolok proyektor/TV lewat kabel input HDMI?",
    "warna_berubah_saat_ditekan": "Apakah warna pigmentasi latar dan bingkai sudut luaran casing monitor menjadi bergelembung cacat begitu sisi frame-nya sedikit aja ditekan ditekan dengan ujung jari Anda?"
}

class ProgramDiagnosaPC:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnosa Pakar PC")
        self.root.geometry("700x700")
        
        # Labeling Judul dan Penjabaran
        tk.Label(root, text="Aplikasi Sistem Pakar Pendiagnosa PC", font=("Segoe UI", 16, "bold"), fg="#2c3e50").pack(pady=(15, 5))
        tk.Label(root, text="Silahkan beri tanda check pada keluhan kelengkapan perangkat Anda:", font=("Segoe UI", 10)).pack(pady=(0, 15))
        
        # Canvas dan Tampilan Frame Scroll 
        container = tk.Frame(root, highlightbackground="#dee2e6", highlightthickness=1)
        container.pack(fill="both", expand=True, padx=25, pady=5)
        self.cvs = tk.Canvas(container, highlightthickness=0)
        self.scr = ttk.Scrollbar(container, orient="vertical", command=self.cvs.yview)
        self.frm_gejala = tk.Frame(self.cvs)
        
        self.frm_gejala.bind("<Configure>", lambda e: self.cvs.configure(scrollregion=self.cvs.bbox("all")))
        self.cvs.create_window((0, 0), window=self.frm_gejala, anchor="nw")
        self.cvs.configure(yscrollcommand=self.scr.set)
        
        self.cvs.pack(side="left", fill="both", expand=True)
        self.scr.pack(side="right", fill="y")
        
        # Rendering Pertanyaan dan Mengambil Variabel Feedback
        self.variabel_check = {}
        for id_gejala, kalimat in daftar_pertanyaan_gejala.items():
            variabel_bool = tk.BooleanVar()
            tk.Checkbutton(self.frm_gejala, text=kalimat, variable=variabel_bool, font=("Segoe UI", 10), wraplength=600, justify="left").pack(anchor="w", pady=4, padx=5)
            self.variabel_check[id_gejala] = variabel_bool
            
        # Pemicu Eksekusi Logika Inferensi Evaluasi Diagnosa
        tk.Button(root, text="Mulai Pengecekan Gejala...", command=self.eksekusi_diagnosa, font=("Segoe UI", 11, "bold"), bg="#1aa75b", fg="white", cursor="hand2", padx=20, pady=5).pack(pady=15)
        
    def eksekusi_diagnosa(self):
        # 1. Mendapatkan Himpunan Subset Terpilih
        jawaban_tercentang = set()
        for id_gejala, variabel_bool in self.variabel_check.items():
            if variabel_bool.get():
                jawaban_tercentang.add(id_gejala)
                
        # 2. Cek Silang Antara Penyakit dan Gejala
        kumpulan_penyakit = []
        for nm_penyakit, dt in aturan_diagnosa.items():
            if dt["gejala"].issubset(jawaban_tercentang):
                kumpulan_penyakit.append((nm_penyakit, dt["solusi"]))
                
        # 3. Lempar Hasil Menuju Interface Graphic Dialog
        if len(kumpulan_penyakit) > 0:
            teks_hasil = "Evaluasi dari sistem pintar pakar ini mendeteksi adanya kejanggalan berikut:\n\n"
            for indeks, (kerusakan, perbaikan) in enumerate(kumpulan_penyakit, 1):
                teks_hasil += f"[{indeks}] KEADAAN DARURAT: {kerusakan}\n    JALAN KELUAR   : {perbaikan}\n\n"
            messagebox.showinfo("Laporan Pakar Berhasil Ditemukan", teks_hasil)
        else:
            pesan_nol = "Sistem gagal menemukan pemetaan kaitan komponen gejala dengan kerusakan di basis data kami.\n\nSaran: Mohon melengkapi keluhan jika terlewat, dan segera merapat ke IT professional terdekat."
            messagebox.showwarning("Proses Analisis Terhambat", pesan_nol)

if __name__ == "__main__":
    app_window = tk.Tk()
    ProgramDiagnosaPC(app_window)
    app_window.mainloop()
