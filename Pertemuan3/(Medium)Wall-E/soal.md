# 🤖 Misi Wall-E: Pengelompokan Benda dengan Divide and Conquer 🌱

## Latar Belakang

Di masa depan yang jauh, Wall-E, robot kecil yang bertugas membersihkan Bumi, menemukan tumpukan benda-benda yang perlu disortir. Setiap benda memiliki rentang waktu tertentu ketika benda tersebut aktif. Wall-E harus mengelompokkan benda-benda ini ke dalam beberapa grup, di mana tidak ada dua benda dalam satu grup yang memiliki waktu aktif yang saling tumpang tindih.

## 🧩 Permasalahan

Diberikan sejumlah benda dengan waktu aktif masing-masing, tentukan jumlah grup minimum yang dibutuhkan untuk mengelompokkan semua benda, sehingga tidak ada benda dalam grup yang sama yang memiliki waktu aktif yang tumpang tindih.

## 📥 Format Input

Sebuah array 2D yang berisi rentang waktu aktif setiap benda. Setiap interval direpresentasikan sebagai `[left_i, right_i]`, yang berarti benda aktif dari detik ke-`left_i` hingga detik ke-`right_i`.

## 📊 Batasan

- 1 ≤ jumlah benda ≤ 10^5
- Setiap interval memiliki 2 elemen: 1 ≤ left_i ≤ right_i ≤ 10^6

## 📤 Format Output

Jumlah grup minimum yang dibutuhkan untuk mengelompokkan semua benda.

## 📋 Contoh

### Contoh 1

**Input:**
```
[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
```

**Output:**
```
3
```

**Penjelasan:**
- Grup 1: [1, 5], [6, 8]
- Grup 2: [2, 3]
- Grup 3: [5, 10], [1, 10]

Kita membutuhkan minimal 3 grup untuk mengelompokkan semua benda tanpa ada tumpang tindih dalam grup yang sama.

### Contoh 2

**Input:**
```
[[1, 3], [5, 6], [8, 10], [11, 13]]
```

**Output:**
```
1
```

**Penjelasan:**
Semua interval tidak bertumpuk, jadi bisa dikelompokkan dalam 1 grup saja.

## 🧠 Analisis Pendekatan

### Pendekatan Divide and Conquer

Solusi menggunakan pendekatan **Divide and Conquer** dengan langkah-langkah berikut:

1. **Langkah Divide (Bagi):**
   - Bagi array interval menjadi dua bagian yang kurang lebih sama besar
   - Rekursif proses setiap bagian

2. **Langkah Conquer (Kuasai):**
   - Selesaikan submasalah untuk bagian kiri dan kanan secara rekursif
   - Dapatkan jumlah grup minimum untuk masing-masing bagian

3. **Langkah Combine (Gabungkan):**
   - Gabungkan hasil dari kedua bagian dengan mempertimbangkan kemungkinan penggabungan grup
   - Untuk melakukan ini, buat grafik konflik antar interval dan gunakan algoritma pencolokan grafik

### Algoritma Detail:

1. Urutkan interval berdasarkan waktu mulai
2. Terapkan divide and conquer:
   - Bagi array menjadi dua bagian
   - Selesaikan setiap bagian secara rekursif
   - Gabungkan dengan menghitung jumlah minimum grup yang diperlukan, mempertimbangkan konflik antar interval dari kedua bagian

## 💻 Analisis Kompleksitas

- **Time Complexity**: O(n² log n) - di mana n adalah jumlah benda
  - Tahap divide: O(log n) level rekursi
  - Tahap combine: O(n²) untuk memeriksa konflik antar interval
  
- **Space Complexity**: O(n) - untuk menyimpan informasi grafik konflik dan status kunjungan

## 🛸 Kesimpulan

Dengan solusi ini, Wall-E dapat dengan efisien mengelompokkan benda-benda berdasarkan waktu aktifnya, memastikan tidak ada konflik dalam satu grup, dan menggunakan jumlah grup minimum yang diperlukan.