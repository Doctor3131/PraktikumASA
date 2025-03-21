# 🐱 Misi Tom: Temukan Tikus Terberat ke-K dengan Divide and Conquer 🐭

## 📖 Latar Belakang
Tom si kucing lapar, tapi dia bukan kucing biasa—dia hanya ingin makan **tikus terberat ke-K**. Kamu, si tikus cerdas, harus menemukan tikus dengan berat yang tepat menggunakan metode **Divide and Conquer** agar tidak dimakan oleh Tom! 🫣

## 🎯 Permasalahan
Diberikan **N** tikus dengan berat masing-masing, cari tikus terberat ke-**K** tanpa harus mengurutkan semuanya. Gunakan algoritma **Divide and Conquer** agar lebih cepat!

## 📥 Format Input
1. Baris pertama berisi dua bilangan bulat **N** (jumlah tikus) dan **K** (urutan tikus terberat yang dicari).
2. Baris kedua berisi **N** bilangan bulat yang merepresentasikan berat masing-masing tikus.

### Contoh Input:
```
5 2
3 1 4 1 5
```

## 📤 Format Output
Sebuah bilangan bulat yang menunjukkan berat tikus ke-K yang paling berat.

### Contoh Output:
```
4
```

## 🛠 Pendekatan Algoritma
Kita menggunakan **QuickSelect**, varian dari **QuickSort**, untuk menemukan elemen ke-K terbesar dengan efisiensi **O(N)** secara rata-rata:

1. **Pilih pivot** dari daftar tikus.
2. **Pisahkan** tikus yang lebih berat ke kiri dan yang lebih ringan ke kanan.
3. **Periksa posisi pivot:**
   - Jika pivot ada di indeks **K-1**, maka itu jawabannya!
   - Jika tidak, cari ke kiri atau ke kanan.
4. **Ulangi langkah-langkah di atas** sampai menemukan tikus ke-K terberat.

## 🔹 Fungsi Penting
### **Partition**
Fungsi ini membagi array berdasarkan pivot:
```python
fungsi partition(arr, kiri, kanan):
    pivot = arr[kanan]
    i = kiri
    untuk j dari kiri hingga kanan - 1:
        jika arr[j] >= pivot:
            tukar(arr[i], arr[j])
            i += 1
    tukar(arr[i], arr[kanan])
    kembalikan i
```

### **QuickSelect**
Fungsi utama untuk mencari tikus ke-K terberat:
```python
fungsi quickSelect(arr, kiri, kanan, K):
    jika kiri == kanan:
        kembalikan arr[kiri]
    
    pivotIndex = partition(arr, kiri, kanan)
    jika pivotIndex == K - 1:
        kembalikan arr[pivotIndex]
    elif pivotIndex > K - 1:
        kembalikan quickSelect(arr, kiri, pivotIndex - 1, K)
    lain:
        kembalikan quickSelect(arr, pivotIndex + 1, kanan, K)
```

## 💻 Kompleksitas Waktu
- **Best Case:** O(N)
- **Worst Case:** O(N²) (jika pivot selalu buruk)
- **Average Case:** O(N) (lebih cepat dari sorting O(N log N))

## 🚀 Kesimpulan
Dengan algoritma **QuickSelect**, kita bisa membantu Tom menemukan tikus terberat ke-K lebih cepat tanpa mengurutkan seluruh daftar! Apakah kamu cukup cepat untuk menyelamatkan dirimu dari Tom? 😱

