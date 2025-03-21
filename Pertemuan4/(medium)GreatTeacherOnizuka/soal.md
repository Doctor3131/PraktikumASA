## **📌 Algoritma Binary Search untuk Mencari Murid yang Hilang**
Pak Onizuka sedang menghitung murid-muridnya yang sudah **berdiri dalam urutan** sebelum masuk ke museum. Namun, ada **satu nomor ID murid yang hilang** di antara mereka.  

Kita akan menggunakan **Binary Search** untuk menemukan nomor ID yang hilang dengan efisien.

---

## **🔍 Analisis Masalah**
Diketahui:
- Murid memiliki **ID dalam range [0, N]**.
- **Ada tepat satu nomor yang hilang** dalam daftar yang **sudah terurut naik (ascending)**.
- **Harus menggunakan Binary Search** untuk mencari nomor yang hilang.

---

## **🧩 Contoh Input & Output**
### ✅ **Contoh 1**
**Input:**
```
5
0 1 2 3 5
```
**Output:**
```
4
```
> **Murid dengan ID 4 hilang** karena urutannya harusnya: `[0, 1, 2, 3, 4, 5]`.

---

### ✅ **Contoh 2**
**Input:**
```
6
0 1 2 3 4 5
```
**Output:**
```
6
```
> Semua ID dari **0 hingga 5** ada, berarti yang hilang adalah **6**.

---

## **🚀 Pendekatan dengan Binary Search**
Karena daftar **sudah terurut**, kita dapat menggunakan **Binary Search** dengan aturan berikut:

1. **Gunakan dua pointer**, `kiri` dan `kanan`, untuk mencari celah di mana nomor yang hilang seharusnya ada.
2. **Perhatikan pola ID**:  
   - Normalnya, **nilai di indeks `i`** seharusnya **sama dengan `i`**.
   - Jika `data[tengah] == tengah`, artinya nomor yang hilang **ada di sebelah kanan** → Geser `kiri = tengah + 1`.
   - Jika `data[tengah] != tengah`, artinya nomor yang hilang **ada di sebelah kiri atau di posisi tengah** → Geser `kanan = tengah - 1`.
3. Ketika **`kiri` dan `kanan` bertemu**, `kiri` akan menjadi **posisi ID yang hilang**.

---

## **📜 Algoritma Binary Search**
**Input**:  
- `N` → jumlah murid.  
- `data[]` → daftar ID murid (terurut dari 0 hingga N dengan 1 hilang).  

**Output**:  
- **Nomor ID yang hilang**.

### **🔢 Langkah-langkah Algoritma**
1. **Inisialisasi** `kiri = 0`, `kanan = N - 1`.
2. **Gunakan Binary Search**:
   - Hitung `tengah = (kiri + kanan) // 2`.
   - Jika **data[tengah] == tengah** → Nomor hilang ada di kanan (`kiri = tengah + 1`).
   - Jika **data[tengah] != tengah** → Nomor hilang ada di kiri (`kanan = tengah - 1`).
3. **Ketika loop selesai**, `kiri` adalah **nomor ID yang hilang**.

---

## **💻 Implementasi Kode (Python)**
```python
def findMissingID(data, N):
    kiri, kanan = 0, N - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        
        if data[tengah] == tengah:
            kiri = tengah + 1  # Cari di sebelah kanan
        else:
            kanan = tengah - 1  # Cari di sebelah kiri
    
    return kiri  # Nomor ID yang hilang

def main():
    N = int(input().strip())  # Baca jumlah murid
    data = list(map(int, input().split()))  # Baca ID murid yang ada
    
    print(findMissingID(data, N))

main()
```

---

## **🛠️ Penjelasan Kode**
1. **Fungsi `findMissingID(data, N)`**:
   - Menggunakan **binary search** untuk menemukan **nomor ID yang hilang**.
   - **Pointer kiri dan kanan** digunakan untuk mempersempit pencarian.
   - Setelah loop selesai, `kiri` akan menunjukkan **nomor ID yang hilang**.

2. **Fungsi `main()`**:
   - **Membaca input** jumlah murid `N`.
   - **Membaca list ID murid** yang tersedia.
   - **Mencetak hasil pencarian** nomor ID yang hilang.

---

## **⏳ Kompleksitas Waktu**
- **Binary Search** bekerja dalam **O(log N)** waktu.
- **Jauh lebih efisien** dibandingkan pencarian linear **O(N)**.

---

## **🎯 Kesimpulan**
✅ **Binary Search** adalah cara **cepat dan efisien** untuk menemukan **nomor ID yang hilang**.  
✅ Kode ini bekerja dalam **O(log N)**, sehingga bisa menangani kasus dengan jumlah murid yang lebih besar dengan lebih cepat.  
✅ **Strategi utama**: **Bandingkan indeks dengan nilai ID**, lalu persempit pencarian ke kiri atau kanan. 🚀