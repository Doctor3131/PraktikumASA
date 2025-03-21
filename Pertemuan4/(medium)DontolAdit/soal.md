
---

### **🟢 Hitung Bola - Tantangan Adit & Denis**  

#### **📝 Deskripsi Soal**  
Suatu hari, Adit, Denis, dan teman-temannya bermain game "Hitung Bola".  
Setiap pemain harus memilih **bola dengan angka tertentu** untuk mencapai jumlah angka yang ditentukan.  

Namun, ada tantangan!  
- Pemain harus menggunakan **jumlah bola seminimal mungkin**.  
- Jika gagal, pemain harus mentraktir **bakso Kang Ujang selama satu bulan**! 🍜  

Tibalah giliran Denis. Ia kebingungan dan meminta bantuan Adit. Sebagai seorang programmer, **bantu Adit menemukan solusi terbaik!**  

---

#### **📌 Format Input**  
- Baris pertama berisi dua bilangan bulat **N** dan **H**:  
  - **N** → Jumlah pilihan angka bola yang tersedia *(1 ≤ N ≤ 100)*.  
  - **H** → Total angka yang harus dicapai *(1 ≤ H ≤ 10⁶)*.  
- Baris kedua berisi **N bilangan bulat**, yaitu daftar angka bola yang dapat digunakan.  
  - Setiap angka bola berada dalam rentang **1 ≤ A[i] ≤ H**.  

---

#### **📌 Format Output**  
Cetak satu bilangan bulat yang menunjukkan **jumlah bola minimum** yang diperlukan untuk mencapai tepat **H**.  
- Jika **tidak mungkin**, cetak `-1`.  

---

#### **📊 Contoh Input & Output**  

**🟡 Contoh 1**  
📥 **Input:**  
```
3 10
1 3 5
```  
📤 **Output:**  
```
2
```  
💡 **Penjelasan:**  
Menggunakan `5 + 5` atau `3 + 3 + 3 + 1`.

---

**🟡 Contoh 2**  
📥 **Input:**  
```
5 7
1 2 4 6 8
```  
📤 **Output:**  
```
2
```  
💡 **Penjelasan:**  
Menggunakan `6 + 1` atau `4 + 2 + 1`.

---

**🟡 Contoh 3**  
📥 **Input:**  
```
5 15
4 6 9 3 5
```  
📤 **Output:**  
```
2
```  
💡 **Penjelasan:**  
Menggunakan `6 + 6 + 3` atau `9 + 3 + 3`.

---

#### **💡 Hint & Pendekatan Solusi**  
Gunakan **Decrease and Conquer** untuk mencari solusi optimal:  
1. **Kurangi nilai H dengan angka bola yang dipilih**, lalu cari solusi optimal untuk sisa nilai.  
2. **Gunakan memoization** untuk menghindari perhitungan berulang.  
3. **Jika mencapai H = 0**, kita sudah menemukan solusi terbaik!  

---

#### **🔍 Kompleksitas Waktu**  
- Dengan optimasi **memoization**, kompleksitas menjadi **O(N × H)** dalam kasus terburuk.  

---

### **💻 Kode Solusi (Python)**
```python
def minBola(H, bola, memo):
    if H == 0:
        return 0  
    if H < 0:
        return float('inf')  
    if H in memo:
        return memo[H]  

    min_bola = float('inf')
    for b in bola:
        min_bola = min(min_bola, 1 + minBola(H - b, bola, memo))

    memo[H] = min_bola  
    return min_bola

def main():
    N, H = map(int, input().split())
    bola = list(map(int, input().split()))

    result = minBola(H, bola, {})
    print(result if result != float('inf') else -1)

main()
```

---

#### **🏆 Kesimpulan**  
- **Algoritma ini membantu Adit menemukan solusi optimal!**  
- Dengan menggunakan pendekatan **Decrease and Conquer**, kita dapat menyelesaikan tantangan ini dengan efisien.  
- **Denis tidak jadi traktir bakso!** 🍜🎉  

---

💡 **Apakah kamu bisa menemukan pendekatan lain yang lebih cepat?** 🤔💭