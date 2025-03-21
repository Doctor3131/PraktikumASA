
---

# **Mencari Angka Hilang dalam Array**
## **Deskripsi Soal**
Pada suatu hari Pak Dengklek sedang mengamati beberapa array yang berisi angka. Array ini memiliki `n` angka dengan elemen yang berada dalam rentang `[0, n]`. Namun, Pak Dengklek menyadari bahwa selalu ada **setidaknya satu angka yang hilang** dalam array tersebut. 

Bantulah Pak Dengklek untuk mencari angka yang hilang tersebut. Jika terdapat lebih dari satu angka yang hilang, maka keluarkan angka yang **terbesar**.

## **Format Input**
- Baris pertama berisi sebuah bilangan bulat `n`, yaitu banyaknya elemen dalam array.
- Baris kedua berisi `n` angka yang terdapat dalam array.

## **Batasan**
- `1 ≤ n ≤ 20000`
- `0 ≤ k ≤ n`

## **Format Output**
Sebuah bilangan bulat yang menyatakan angka terbesar yang hilang dari array tersebut.

## **Contoh**
### **Input 1**
```
3
3 0 1
```
### **Output 1**
```
2
```
**Penjelasan**  
Pada array di atas terdapat `3` elemen, sehingga angka dalam rentang `[0, 3]`. Angka yang hilang adalah `2`.

---

### **Input 2**
```
2
1 1
```
### **Output 2**
```
2
```
**Penjelasan**  
Pada array di atas terdapat `2` elemen, sehingga angka dalam rentang `[0, 2]`. Angka yang hilang adalah `0` dan `2`. Karena angka yang hilang terbesar adalah `2`, maka `2` menjadi output.

## **Implementasi dalam Python**
Berikut adalah solusi menggunakan **Binary Search** dengan pendekatan **Reduce and Conquer**:
```python
def cariAngka(data, n):
    dataSet = set(data)
    
    def binarySearch(kiri, kanan):
        if kiri > kanan:
            return kiri - 1
        
        if kiri == kanan:
            if kiri in dataSet:
                return kiri - 1
            else:
                return kiri
        
        tengah = (kiri + kanan) // 2
        
        if tengah not in dataSet:
            return binarySearch(tengah + 1, kanan)
        else:
            kanan_result = binarySearch(tengah + 1, kanan)
            if kanan_result > tengah:
                return kanan_result
            return binarySearch(kiri, tengah - 1)
    
    return binarySearch(0, n)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    hasil = cariAngka(data, n)
    print(hasil)

main()
```

## **Penjelasan Algoritma**
1. **Konversi Array ke `set`**  
   - Menggunakan `set(data)` agar pencarian angka lebih efisien dengan **O(1)**.
  
2. **Implementasi Binary Search**  
   - Cari angka yang hilang dalam rentang `[0, n]`.
   - Jika `tengah` **tidak ada** di `set`, lanjutkan pencarian di sisi **kanan**.
   - Jika `tengah` **ada**, lanjutkan pencarian di sisi **kiri**.

3. **Optimasi**  
   - Menggunakan **Divide and Conquer** untuk mempercepat pencarian dari **O(n) ke O(log n)**.

## **Kompleksitas Waktu**
- **Binary Search**: `O(log n)`
- **Konversi ke `set`**: `O(n)`
- **Total**: **O(n + log n) ≈ O(n)** (cukup cepat untuk `n ≤ 20000`)

## **Kesimpulan**
Pendekatan **Reduce and Conquer** dengan **Binary Search** mempercepat pencarian angka hilang, terutama untuk jumlah data yang besar.

---