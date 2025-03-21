# **Misi: Minimalkan Waktu Pengumpulan Petunjuk**

## **Deskripsi**
Loid Forger tengah menangani sebuah kasus misterius yang membutuhkan sejumlah petunjuk untuk dipecahkan. Ia memiliki tim agen rahasia, di mana setiap agen memiliki **peringkat** yang menggambarkan kecepatan mereka dalam mengumpulkan petunjuk.

Diberikan sebuah array **ranks** di mana `ranks[i]` mewakili peringkat agen ke-`i`. Seorang agen dengan peringkat `r` dapat mengumpulkan `n` petunjuk dalam waktu `r * n²` menit.

Selain itu, diberikan sebuah integer **clue** yang mewakili total jumlah petunjuk yang harus dikumpulkan untuk menyelesaikan kasus tersebut.

Semua agen bekerja secara bersamaan dan **Loid ingin meminimalkan waktu** yang diperlukan untuk mengumpulkan seluruh petunjuk. Tugas Anda adalah menentukan **waktu minimum** yang diperlukan agar seluruh petunjuk dapat dikumpulkan.

---

## **Format Input**
- **Baris pertama**: Array bilangan bulat `ranks`, berisi peringkat masing-masing agen.
- **Baris kedua**: Sebuah bilangan bulat `clue`, yaitu jumlah total petunjuk yang harus dikumpulkan.

### **Constraints**
- `1 ≤ jumlah agen (ranks.length) ≤ 10⁵`
- `0 ≤ ranks[i] ≤ 100`
- `1 ≤ jumlah petunjuk (clue) ≤ 10⁶`

---

## **Format Output**
- Sebuah bilangan bulat yang menunjukkan **waktu minimum** yang diperlukan untuk mengumpulkan seluruh petunjuk.

---

## **Contoh Input & Output**

### **Sample Input 0**
```
4 2 3 1
10
```

### **Sample Output 0**
```
16
```

### **Penjelasan**
- Agen dengan peringkat `4` mengumpulkan `2` petunjuk dalam waktu `4 * 2² = 16` menit.
- Agen dengan peringkat `2` mengumpulkan `2` petunjuk dalam waktu `2 * 2² = 8` menit.
- Agen dengan peringkat `3` mengumpulkan `2` petunjuk dalam waktu `3 * 2² = 12` menit.
- Agen dengan peringkat `1` mengumpulkan `4` petunjuk dalam waktu `1 * 4² = 16` menit.
- Waktu maksimum dari agen yang bekerja adalah **16 menit**.

---

### **Sample Input 1**
```
5 1 8
6
```

### **Sample Output 1**
```
16
```

### **Penjelasan**
- Agen dengan peringkat `5` mengumpulkan `1` petunjuk dalam waktu `5 * 1² = 5` menit.
- Agen dengan peringkat `1` mengumpulkan `4` petunjuk dalam waktu `1 * 4² = 16` menit.
- Agen dengan peringkat `8` mengumpulkan `1` petunjuk dalam waktu `8 * 1² = 8` menit.
- Waktu maksimum dari agen yang bekerja adalah **16 menit**.

---

## **Solusi dengan Binary Search**
Karena kita ingin **menemukan waktu minimum**, kita bisa menggunakan **Binary Search** untuk mencari batas atas dari waktu yang diperlukan.

### **Langkah-langkah Algoritma**
1. Tetapkan rentang pencarian dari **0** hingga **max(ranks) * clue²** (batas maksimum waktu).
2. Gunakan **Binary Search** untuk menemukan waktu minimal `T` yang memungkinkan pengumpulan `clue` petunjuk.
3. Cek apakah `T` cukup dengan menghitung total petunjuk yang bisa dikumpulkan dalam waktu tersebut.

### **Implementasi dalam Python**
```python
# Fungsi untuk menghitung jumlah petunjuk yang bisa dikumpulkan dalam waktu tertentu
def dapat_mengumpulkan(ranks, clue, waktu):
    total = 0
    for r in ranks:
        n = 1
        while r * n * n <= waktu:  # Selama waktu masih mencukupi untuk mengumpulkan petunjuk tambahan
            total += 1
            if total >= clue:  # Jika sudah cukup
                return True
            n += 1
    return total >= clue

# Binary Search untuk mencari waktu minimum
def waktu_minimum(ranks, clue):
    kiri, kanan = 0, max(ranks) * clue * clue  # Batas maksimum waktu
    while kiri < kanan:
        tengah = (kiri + kanan) // 2
        if dapat_mengumpulkan(ranks, clue, tengah):
            kanan = tengah  # Coba cari waktu yang lebih kecil
        else:
            kiri = tengah + 1
    return kiri

# Membaca input
def main():
    ranks = list(map(int, input().split()))  # Membaca array ranks
    clue = int(input())  # Membaca jumlah petunjuk
    print(waktu_minimum(ranks, clue))

main()
```

### **Kompleksitas Waktu**
- **Binary Search** bekerja dalam **O(log(max_time))**.
- Untuk setiap pencarian, kita **menghitung petunjuk dalam O(N)**.
- Total kompleksitas: **O(N log(max_time))**, cukup cepat untuk batasan **N ≤ 10⁵**.

Dengan algoritma ini, **Loid dapat menyelesaikan misinya dengan efisien dan cepat!** 🕵️✨

