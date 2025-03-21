## 📌 **Pencarian Bilangan dalam Daftar dengan Binary Search**

### **📝 Deskripsi Soal**
Si A memiliki sebuah daftar (list) yang berisi bilangan integer yang **sudah terurut** (baik dari **terkecil ke terbesar** atau **terbesar ke terkecil**).  
Tugas kita adalah mencari suatu bilangan dalam daftar tersebut menggunakan **algoritma binary search**.  

Jika angka **ditemukan**, kita mengembalikan **index** dari angka tersebut dalam daftar.  
Jika angka **tidak ditemukan**, kita mengembalikan **"Tidak ditemukan"**.

---

### **📥 Format Input**
1. Baris pertama: Daftar bilangan dalam format **list**  
   - Bisa berupa list kosong `[]` atau list berisi angka `[1,2,3,4,5]`
2. Baris kedua: Bilangan integer yang ingin dicari dalam daftar

---

### **📤 Format Output**
- Jika angka ditemukan: **Index dari angka dalam daftar**  
- Jika angka tidak ditemukan: `"Tidak ditemukan"`

---

### **📌 Constraints**
- List selalu dalam keadaan **terurut** (ascending atau descending)
- Bilangan yang dicari adalah **integer**
- Jika list kosong, selalu mengembalikan **"Tidak ditemukan"**

---

### **🧩 Contoh Input & Output**

#### ✅ **Contoh 1 (Daftar Kosong)**
**Input:**
```
[]
4
```
**Output:**
```
"Tidak ditemukan"
```
> Karena daftar kosong, angka 4 pasti tidak ditemukan.

---

#### ✅ **Contoh 2 (Ascending List)**
**Input:**
```
[1,2,3,4,5]
3
```
**Output:**
```
2
```
> **Angka 3** ditemukan di **index ke-2**.

---

#### ✅ **Contoh 3 (Descending List)**
**Input:**
```
[9,8,7,6,5,4,3,2,1]
4
```
**Output:**
```
5
```
> **Angka 4** ditemukan di **index ke-5**.

---

### **🚀 Solusi: Algoritma Binary Search**
**Binary Search** adalah algoritma pencarian yang bekerja dengan cara **membagi daftar menjadi dua bagian** secara berulang hingga menemukan angka yang dicari.  
Langkah-langkahnya:
1. Cek apakah **list kosong** → Jika ya, langsung return `"Tidak ditemukan"`.
2. Tentukan apakah list **terurut naik (ascending) atau turun (descending)**.
3. Gunakan **binary search**:
   - Tentukan **nilai tengah** dari daftar.
   - Jika angka di tengah adalah **target**, return index tengah.
   - Jika angka di tengah **lebih kecil dari target** (dalam **ascending list**) → Cari ke **kanan**.
   - Jika angka di tengah **lebih besar dari target** (dalam **descending list**) → Cari ke **kanan**.
   - Jika tidak, cari ke kiri.
4. Jika angka tidak ditemukan setelah semua pencarian, return **"Tidak ditemukan"**.

---

### **💻 Kode Implementasi**
```python
def binarySearch(data, target):
    if not data:
        return "Tidak ditemukan"

    kiri, kanan = 0, len(data) - 1
    isUrutNaik = data[0] < data[-1]

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data[tengah] == target:
            return tengah
        elif (data[tengah] < target and isUrutNaik) or (data[tengah] > target and not isUrutNaik):
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return "Tidak ditemukan"

def main():
    try:
        data_input = input().strip()
        if data_input == "[]":
            data = []
        else:
            data = list(map(int, data_input.strip("[]").split(",")))
        
        target = int(input().strip())
        print(binarySearch(data, target))
    
    except ValueError:
        print("Input tidak valid")

main()
```

---

### **🛠️ Penjelasan Kode**
1. **Fungsi `binarySearch(data, target)`**  
   - Mengecek apakah **daftar kosong** → Jika ya, return `"Tidak ditemukan"`.
   - Menentukan apakah **list terurut naik atau turun**.
   - Melakukan **binary search** dengan loop:
     - **Cek angka tengah**, jika cocok return index.
     - Jika angka tengah lebih kecil/besar dari target, cari ke kiri atau kanan.
   - Jika tidak ditemukan, return **"Tidak ditemukan"**.

2. **Fungsi `main()`**  
   - **Mengambil input list** dalam format `[1,2,3,4,5]`.
   - **Menangani input kosong** (`[]`).
   - **Konversi list ke integer** menggunakan `map(int, ...)`.
   - **Membaca target angka**.
   - **Menangani error input** dengan `try-except`.

---

### **⏳ Kompleksitas Waktu**
- **Best case** (angka langsung ditemukan) → **O(1)**
- **Worst case** (harus menyaring semua angka) → **O(log N)**  
  → **Lebih efisien** daripada linear search **O(N)**!

---

### **🎯 Kesimpulan**
✅ **Binary Search** adalah algoritma pencarian **efisien** untuk daftar **terurut**.  
✅ Kode ini menangani **daftar kosong**, **list ascending atau descending**, dan **kesalahan input**.  
✅ Dengan **O(log N)**, algoritma ini jauh lebih cepat dibandingkan pencarian linear! 🚀