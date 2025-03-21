# 🍰 Petualangan Bisnis Kue Pangeran Pastry Mille Morteln 🍰

## 📜 Latar Belakang

Di sebuah kerajaan yang jauh bernama Morteln, seorang pangeran bungsu bernama **Pastry Mille Morteln** memutuskan untuk mengejar impiannya. Daripada menghabiskan waktu di istana, ia memilih untuk membuka toko roti miliknya sendiri!

Dengan semangat yang membara, Pangeran Pastry:
- 🛒 Membeli semua bahan-bahan berkualitas terbaik
- 🔮 Mendapatkan oven ajaib yang dapat memanggang berbagai jenis kue
- 🏪 Membuka toko roti yang cantik di pusat kota

## 💰 Masalah Bisnis

Sayangnya, bisnis tidak selalu berjalan mulus. Pengeluaran mulai melebihi pendapatan! 😱

Sebagai pengusaha yang cerdas, Pangeran Pastry memutuskan untuk:
1. Mempelajari pasar permen
2. Menemukan strategi baru untuk meningkatkan keuntungan

## 🧠 Strategi Baru

Pangeran Pastry menemukan bahwa:

> **Mengemas kue dalam kotak sangat menguntungkan!** 📦
> 
> Nilai kotak = Jumlah jenis kue berbeda dalam kotak
> 
> Semakin tinggi nilai kotak, semakin tinggi harganya! 💎

## ⚙️ Kendala Produksi

Namun ada masalah:

- 🎭 Oven ajaib memiliki "kehendak sendiri"
- 🔄 Oven memilih jenis kue yang akan dipanggang
- ❌ Pastry tidak dapat memengaruhi pilihan oven

**Yang diketahui Pastry:**
- Urutan dan jenis kue yang akan dipanggang hari ini
- Dia harus mengemas kue-kue dalam tepat **k** kotak
- Setiap kotak harus berisi segmen kue yang berurutan
- Setiap kotak harus memiliki minimal 1 kue

## 🎯 Tujuan

Pastry Mille Morteln perlu **memaksimalkan nilai total** dari semua kotak kue.

## 📊 Contoh Kasus

### 📦 Contoh 1:
```
Input:
4 1
1 2 2 1

Output:
2
```

**Analisis:**
- Pastry memiliki 4 kue dengan jenis: [1, 2, 2, 1]
- Hanya ada 1 kotak, jadi semua kue masuk ke dalamnya
- Kotak berisi 2 jenis kue berbeda (1 dan 2)
- Nilai total = 2

### 📦 Contoh 2:
```
Input:
7 2
1 3 3 1 4 4 4

Output:
5
```

**Analisis:**
- Pastry memiliki 7 kue dengan jenis: [1, 3, 3, 1, 4, 4, 4]
- Ada 2 kotak yang harus diisi
- Pembagian optimal:
  - Kotak 1: [1, 3] → Nilai = 2 (dua jenis berbeda)
  - Kotak 2: [3, 1, 4, 4, 4] → Nilai = 3 (tiga jenis berbeda)
- Nilai total = 2 + 3 = 5

## 📝 Format Input

```
n k
type₁ type₂ ... typeₙ
```

- **n**: jumlah kue (1 ≤ n ≤ 35000)
- **k**: jumlah kotak (1 ≤ k ≤ min(n, 50))
- **typeᵢ**: jenis kue ke-i

## 🔢 Format Output

```
Nilai total maksimum yang mungkin
```

## 💡 Pendekatan Solusi

### Algoritma Divide and Conquer

Masalah ini dapat diselesaikan dengan membagi masalah menjadi submasalah yang lebih kecil:

1. **Divide**: Membagi rangkaian kue menjadi dua bagian
2. **Conquer**: Menyelesaikan masing-masing bagian secara independen
3. **Combine**: Menggabungkan solusi-solusi untuk mendapatkan nilai maksimum

### Pseudocode

```
function hitungNilaiMax(kue, n, k):
    // Menghitung nilai semua segmen
    nilai[0...n-1][0...n-1] = hitungNilaiSegmen(kue, n)
    
    // Menyelesaikan dengan divide and conquer
    return divideConquer(nilai, 0, n-1, k, memo={})

function divideConquer(nilai, awal, akhir, k, memo):
    // Basis case
    if k == 1:
        return nilai[awal][akhir]
    
    if (awal, akhir, k) in memo:
        return memo[awal, akhir, k]
    
    hasilTerbaik = 0
    
    // Mencoba semua kemungkinan pemisahan
    for i = awal to akhir-1:
        for kiri = 1 to k-1:
            kanan = k - kiri
            
            if kiri dan kanan valid:
                nilaiKiri = divideConquer(nilai, awal, i, kiri, memo)
                nilaiKanan = divideConquer(nilai, i+1, akhir, kanan, memo)
                hasilTerbaik = max(hasilTerbaik, nilaiKiri + nilaiKanan)
    
    memo[awal, akhir, k] = hasilTerbaik
    return hasilTerbaik
```

## 🔍 Analisis Kompleksitas

- **Waktu**: O(n³k) - dalam kasus terburuk
- **Ruang**: O(n²k) - untuk memoization

## 🌟 Kesimpulan

Dengan algoritma Divide and Conquer yang tepat, Pangeran Pastry Mille Morteln dapat menentukan cara optimal untuk mengemas kue-kuenya, memaksimalkan keuntungan, dan menyelamatkan bisnis rotinya yang sedang berkembang!

---

*"Setiap pengusaha sukses adalah seorang pemecah masalah yang baik." - Pangeran Pastry Mille Morteln*