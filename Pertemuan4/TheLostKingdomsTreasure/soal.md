<!-- PREVIEW CTRL SHIFT V -->

# 🏰 Misi Fakhrell: Menemukan Gua Terbesar! 🏆

## 📖 Latar Belakang
King Farid dari **kerajaan kuno Gondang** telah menyembunyikan **harta karun berharga** di dalam gua yang luas dan bercabang-cabang.  
Namun, **peta kerajaan telah hilang!** 📜  
Satu-satunya petunjuk yang tersisa adalah sebuah **buku kuno berisi angka-angka misterius**.  

Pangeran **Fakhrell** harus menemukan bagian **terbesar dari gua** untuk mempersempit pencariannya.  
Bantu dia menggunakan **algoritma Divide and Conquer** untuk menemukan **bagian gua terbesar** sebelum para pencuri menemukannya lebih dulu! 💎🏆

---

## 📥 Format Input
1. **Baris pertama**: Satu bilangan bulat **N** _(1 ≤ N ≤ 100.000)_ → jumlah bagian gua.  
2. **Baris kedua**: N bilangan bulat yang dipisahkan oleh spasi, menyatakan ukuran setiap bagian gua.  
   - Nilai setiap bagian **-10⁹ ≤ A[i] ≤ 10⁹**.

---

## 📤 Format Output
Cetak **satu bilangan bulat** yang merupakan ukuran **terbesar dari bagian gua**.

---

## 📌 Contoh Input & Output

### 🎯 Contoh 1
#### **Input**
5 3 1 4 1 5
#### **Output**
5

---

### 🎯 Contoh 2
#### **Input**
10 -2 -3 -1 -7 -4 -6 -8 -5 -9 -10
#### **Output**
-1

---

### 🎯 Contoh 3
#### **Input**
7 10 20 -30 40 -50 60 70
#### **Output**
70

---

## 🛠️ Penyelesaian dengan **Divide and Conquer**
Karena **N bisa mencapai 100.000**, kita perlu menggunakan pendekatan yang **efisien**.  
Pendekatan **Divide and Conquer** memungkinkan kita menemukan nilai maksimum dengan **O(N log N)**.

### 🔍 **Langkah-langkah Algoritma:**
1. **Bagi array menjadi dua bagian** _(Divide)_.
2. **Cari nilai maksimum di setiap bagian secara rekursif** _(Conquer)_.
3. **Gabungkan hasil dari dua bagian** untuk mendapatkan nilai maksimum keseluruhan _(Combine)_.

---

## 🚀 Tantangan untukmu!
Bisakah kamu menerapkan **algoritma Divide and Conquer** untuk membantu **Fakhrell** menemukan gua terbesar?  
Coba buat implementasinya dalam **Python, C++, atau bahasa favoritmu!** 💻🔥  

Semoga sukses dalam misi mencari **gua terbesar** dan menemukan **harta karun King Farid**! 🏆💰
