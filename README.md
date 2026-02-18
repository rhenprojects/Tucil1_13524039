# Tucil1_13524039
## Penyelesaian Permainan Queens LinkedIn dengan Algoritma Brute Force

---

## 1. Deskripsi Singkat Program

Program ini dibuat untuk menyelesaikan permainan **Queens LinkedIn** menggunakan algoritma *brute force*.

Permainan dimainkan pada papan berukuran **N x N** yang terdiri atas blok-blok berwarna. Aturan permainan adalah sebagai berikut:

1. Setiap blok berwarna memiliki tepat satu ratu.
2. Setiap baris memiliki tepat satu ratu.
3. Setiap kolom memiliki tepat satu ratu.
4. Tidak ada dua ratu yang boleh saling bersebelahan, termasuk secara diagonal.
5. Dua ratu diperbolehkan berada pada diagonal yang sama selama tidak menempati kotak yang bersebelahan.

Program membaca konfigurasi warna papan dari file `.txt`, kemudian menghasilkan solusi dengan mencoba seluruh kemungkinan permutasi posisi ratu hingga ditemukan konfigurasi yang valid.

---

## 2. Requirement Program

Program ini dibuat menggunakan:

- Python 3.x
- Library bawaan Python:
  - `itertools`
  - `time`
  - `os`

Tidak diperlukan instalasi library tambahan.

## 3. Cara Mengkompilasi Program

Program ini dibuat menggunakan Python (bahasa interpreted), sehingga **tidak perlu dikompilasi** sebelum dijalankan.

Untuk mengecek versi Python:

```bash
python --version
```

---

## 4. Cara Menjalankan dan Menggunakan Program

### A. Menjalankan Program

1. Buka terminal / command prompt.
2. Masuk ke direktori utama repository:

```bash
cd Tucil1_13524039
```

3. Jalankan program dengan perintah:

```bash
python src/tucil.py
```
---

### B. Cara Menggunakan Program

1. Program akan menampilkan daftar file test case yang tersedia pada folder:

```
test/test_cases
```

2. Masukkan nomor test case yang ingin dijalankan.

3. Program akan:
   - Membaca konfigurasi papan dari file yang dipilih
   - Mencari solusi menggunakan algoritma brute force
   - Menampilkan hasil akhir board
   - Menampilkan waktu pencarian
   - Menampilkan jumlah kasus yang ditinjau

4. Setelah solusi ditemukan, program akan menanyakan apakah solusi ingin disimpan.

5. Jika memilih **"ya"**, maka solusi akan disimpan pada folder:

```
test/test_solutions
```

dengan format nama file:

```
solusi_namafiletestcase.txt
```

Contoh:

```
case1.txt → solusi_case1.txt
```

---

## 5. Author

Nama  : Rhenaldy Cahyadi Putra
NIM   : 13524039
Kelas : K-01
