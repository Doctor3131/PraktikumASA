# Soal: Menempatkan Kuda ke Kandang dengan Koefisien Ketidakbahagiaan Minimal

## **Deskripsi Masalah**
Setiap hari, Shiroe mengeluarkan semua kudanya agar mereka dapat berlari dan bermain. Setelah selesai, petani Ion harus membawa semua kuda kembali ke kandang. Untuk melakukan ini, ia menempatkan mereka dalam garis lurus dan memandu mereka ke kandang.

Karena kuda-kuda sudah lelah, Ion ingin mengurangi pergerakan mereka seminimal mungkin. Oleh karena itu, ia menggunakan algoritma berikut:
- Kuda pertama masuk ke kandang pertama, kuda kedua ke kandang kedua, dan seterusnya.
- Ion tidak ingin ada kandang yang kosong.
- Semua kuda harus ditempatkan dalam kandang.

Ion memiliki **dua jenis kuda**, yaitu **hitam (1)** dan **putih (0)**. Namun, kuda hitam dan putih tidak terlalu akur. Jika dalam satu kandang terdapat *i* kuda hitam dan *j* kuda putih, maka **koefisien ketidakbahagiaan** dari kandang itu adalah **i × j**.

Tugas Anda adalah menentukan cara menempatkan **N kuda ke dalam K kandang**, sehingga **total koefisien ketidakbahagiaan** di semua kandang menjadi **minimal**.

---
## **Format Input**
- Baris pertama berisi dua bilangan bulat **n** dan **k**, di mana:
  - **n** adalah jumlah kuda (*1 ≤ n ≤ 500*)
  - **k** adalah jumlah kandang (*1 ≤ k ≤ n*)
- Baris berikutnya berisi **N bilangan bulat** yang merepresentasikan warna masing-masing kuda dalam urutan:
  - **1** berarti kuda hitam
  - **0** berarti kuda putih

---
## **Format Output**
Sebuah bilangan bulat yang menunjukkan **total koefisien ketidakbahagiaan minimal** setelah semua kuda ditempatkan ke dalam **K kandang**.

---
## **Contoh**
### **Input 1:**
```
6 3
1
1
0
1
0
1
```
### **Output 1:**
```
2
```
### **Penjelasan:**
Salah satu cara membagi kuda ke dalam **3 kandang** dengan ketidakbahagiaan minimal:
1. Kandang 1: (1,1) → **0** (karena tidak ada kuda putih)
2. Kandang 2: (0,1) → **1 × 1 = 1**
3. Kandang 3: (0,1) → **1 × 1 = 1**
Total = **1 + 1 = 2**

---
## **Batasan**
- **1 ≤ n ≤ 500**
- **1 ≤ k ≤ n**
- Semua kuda harus ditempatkan, dan semua kandang harus terisi.

