<!-- PREVIEW CTRL SHIFT V -->

# 🏆 Bantu Sung Jin-Woo Menyiapkan Item ke Dungeon Terakhir!

## 📖 Latar Belakang
Sung Jin-Woo sedang bersiap untuk menghadapi **Dungeon Level 100**, tantangan terberat yang pernah ia hadapi! Namun, sebelum itu, ia perlu menjual beberapa barang berharga yang ia temukan di dungeon sebelumnya. Setiap barang memiliki nilai tertentu, dan Sung Jin-Woo harus memilih **tiga barang** yang urutannya meningkat dalam **dua daftar berbeda**:

1. **Kekuatan barang**
2. **Harga jual di toko**

Tugas kita adalah mencari kombinasi tiga barang yang memiliki **urutan meningkat di kedua daftar**. Dengan memilih barang yang tepat, Sung Jin-Woo bisa **memaksimalkan keuntungan** dan membeli perlengkapan yang ia butuhkan untuk pertarungan terakhir! ⚔️🔥

---

## 🎯 Tugas
Diberikan dua daftar barang yang merupakan permutasi dari angka **0 hingga n-1**, kita perlu menghitung **berapa banyak kombinasi tiga barang** yang memiliki urutan meningkat di kedua daftar tersebut.

---

## 📥 Format Input
- **Array pertama**: Menunjukkan urutan barang berdasarkan **kekuatan**.
- **Array kedua**: Menunjukkan urutan barang berdasarkan **harga jual**.

- Kedua array memiliki panjang **n**, dengan **3 ≤ n ≤ 100.000**.
- Setiap angka dalam array adalah **permutasi** dari `[0, 1, ..., n-1]`.

### 📝 Contoh Input 1:
```
2 0 1 3  
0 1 2 3
```

### 📝 Contoh Input 2:
```
4 0 1 3 2
4 1 0 2 3
```

---

## 📤 Format Output
Satu bilangan bulat yang menunjukkan jumlah kombinasi **tiga barang** yang memenuhi aturan peningkatan urutan di **kedua daftar**.

### 🎯 Contoh Output 1:
```
1
```
### 🎯 Contoh Output 2:
```
4
```

---

## 📌 Penjelasan
Untuk contoh pertama:
- **Daftar kekuatan barang**: `2, 0, 1, 3`
- **Daftar harga jual**: `0, 1, 2, 3`

Kemungkinan kombinasi urutan meningkat di **nums1**:
- `(2,0,1)` ❌ Tidak meningkat
- `(2,0,3)` ❌ Tidak meningkat
- `(2,1,3)` ❌ Tidak meningkat
- `(0,1,3)` ✅ Meningkat di nums1 dan nums2

Hanya satu kombinasi `(0,1,3)` yang valid, sehingga **output = 1**.

---

## 🏅 Tantangan untukmu!
Bisakah kamu membuat algoritma yang **efisien** untuk menyelesaikan tantangan ini? Ingat, **n bisa mencapai 100.000**! 🚀

Semoga berhasil, Hunter! ⚔️🔥

