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

Tidak diperlukan instalasi library tambahan.

Untuk memastikan Python telah terpasang:

```bash
python --version