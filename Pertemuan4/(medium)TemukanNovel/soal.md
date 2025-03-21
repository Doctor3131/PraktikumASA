
---

### 📌 **Binary Search - Mencari Indeks Awal & Akhir**
#### **📖 Deskripsi Soal**
Soobin memiliki koleksi novel *Omniscient Reader* yang tertata dalam array berdasarkan urutan volumenya.  
Soobin ingin mengetahui **di mana volume yang dicari berada** dalam koleksinya.  
Bantu Soobin untuk menemukan **indeks awal dan akhir** dari volume yang dicari dengan **algoritma Binary Search**.

Jika volume yang dicari tidak ditemukan, maka akan mengeluarkan output **[-1, -1]**.

---

### **📥 Format Input**
1. **Baris pertama**: Array integer yang sudah terurut.  
2. **Baris kedua**: Target volume yang dicari *(integer)*.

---

### **📤 Format Output**
Array yang berisi **posisi awal dan akhir** dari target yang dicari:  
`[awal, akhir]`  
Jika tidak ditemukan, cetak:  
`[-1, -1]`  

---

### **📊 Contoh Input & Output**
#### **🟢 Contoh 1**
📥 **Input:**  
```
1 1 3 5 6 9 9
1
```
📤 **Output:**  
```
[0, 1]
```
💡 **Penjelasan:**  
Target `1` ditemukan pertama kali di indeks **0** dan terakhir di indeks **1**.

---

#### **🟢 Contoh 2**
📥 **Input:**  
```
1 2 3 4 5
8
```
📤 **Output:**  
```
[-1, -1]
```
💡 **Penjelasan:**  
Target `8` **tidak ditemukan** dalam array, sehingga output adalah `[-1, -1]`.

---

### **🔎 Algoritma Binary Search**
Pendekatan **Binary Search** digunakan karena array **sudah terurut**.  
Kita melakukan dua pencarian terpisah:  
1. **`findFirstPosition(arr, target)`** → Mencari **indeks pertama** dari `target`.  
2. **`findLastPosition(arr, target)`** → Mencari **indeks terakhir** dari `target`.  
3. **`searchRange(arr, target)`** → Menggabungkan hasil kedua pencarian.

---

### **🕒 Kompleksitas Waktu**
- **Binary Search** memiliki kompleksitas **O(log N)** untuk masing-masing pencarian.  
- Total waktu eksekusi **O(2 × log N) ≈ O(log N)**, yang jauh lebih efisien dibandingkan pencarian linear **O(N)**.

---

### **✅ Kesimpulan**
- **Binary Search** adalah pendekatan optimal untuk **mencari rentang indeks** dalam array terurut.  
- **Jika nilai ditemukan**, kita dapat dengan cepat mendapatkan indeks awal dan akhir.  
- **Jika tidak ditemukan**, kita langsung mengembalikan `[-1, -1]`.  
- **Waktu eksekusi cepat**, bahkan untuk array besar.

🔹 **Bisakah kamu mengoptimalkan kode lebih lanjut?** 🤔💡