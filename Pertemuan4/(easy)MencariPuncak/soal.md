# **Misi: Menemukan Puncak Tertinggi Gunung Ashenfang**

## **Deskripsi**

Kamu adalah seorang petualang ternama yang tengah memburu relic legendaris, sebuah artefak langka yang dikabarkan mampu membangkitkan orang yang telah tiada. Menurut desas-desus, relic itu tersembunyi di sebuah kuil kuno di puncak Gunung Ashenfang. Namun, gunung ini bukanlah tempat biasa. Ia diselimuti kabut tebal yang menyesatkan dan dipenuhi makhluk buas yang siap menerkam siapa saja yang nekat mendakinya.

Pegunungan ini memiliki karakteristik unik yaitu terdiri dari satu punggungan yang terus menanjak hingga mencapai titik tertinggi, lalu menurun tanpa ada dua titik berdekatan yang memiliki ketinggian yang sama.

Legenda setempat menyebutkan bahwa siapa pun yang berdiri di Singgasana Surga saat titik balik matahari akan dianugerahi kebijaksanaan luar biasa. Namun, waktu sangat terbatas—kamu hanya memiliki cukup sinar matahari untuk melakukan sejumlah pencarian secara logaritmik sebelum malam tiba dan kegelapan menelan segalanya.

Kamu memiliki sebuah peta yang menunjukkan ketinggian di setiap titik sepanjang punggungan. Misinya jelas: **temukan puncak tertinggi dan tentukan dengan tepat di mana letaknya sebelum waktu habis!** (posisi index)

---

## **Format Input**

1. Baris pertama berisi bilangan bulat positif **n**, yaitu panjang/banyak titik punggungan.
2. Baris kedua berisi **n** bilangan bulat positif yang merepresentasikan ketinggian titik-titik punggungan dalam urutan tertentu.

### **Constraints**
- `1 <= n <= 10^5`
- `1 <= ketinggian <= 10^9`
- Punggungan selalu memiliki bentuk **gunung** (menanjak hingga puncak lalu menurun)

---

## **Format Output**

- Sebuah bilangan bulat positif yang menunjukkan **index dari puncak pegunungan tersebut**.
- **Index array dimulai dari 1**.

---

## **Contoh Input & Output**

### **Sample Input 0**
```
9
1 4 23 79 84 99 95 91 21
```

### **Sample Output 0**
```
6
```

---

## **Solusi dengan Binary Search**

Karena data berbentuk gunung (menaik lalu menurun) dan kita perlu menemukan puncaknya, kita bisa menggunakan **Binary Search** untuk mencari elemen maksimum dalam waktu **O(log n)**.

### **Langkah-langkah algoritma:**
1. Inisialisasi `kiri = 0` dan `kanan = n - 1`.
2. Gunakan Binary Search:
   - Hitung `tengah = (kiri + kanan) // 2`.
   - Jika `data[tengah] > data[tengah + 1]`, maka puncak ada di kiri (termasuk `tengah`). Update `kanan = tengah`.
   - Jika `data[tengah] < data[tengah + 1]`, maka puncak ada di kanan. Update `kiri = tengah + 1`.
3. Saat `kiri == kanan`, kita telah menemukan puncak.

### **Implementasi dalam Python**
```python
# Fungsi untuk mencari puncak menggunakan Binary Search
def find_peak(data):
    kiri, kanan = 0, len(data) - 1
    
    while kiri < kanan:
        tengah = (kiri + kanan) // 2
        
        if data[tengah] > data[tengah + 1]:
            kanan = tengah  # Puncak ada di kiri (termasuk tengah)
        else:
            kiri = tengah + 1  # Puncak ada di kanan
    
    return kiri + 1  # Konversi ke index 1-based

# Membaca input
def main():
    n = int(input())  # Membaca jumlah titik
    data = list(map(int, input().split()))  # Membaca ketinggian
    print(find_peak(data))

main()
```

### **Kompleksitas Waktu**
- **Binary Search** bekerja dalam **O(log n)** waktu, yang jauh lebih efisien dibanding pencarian linear **O(n)**.

Dengan algoritma ini, kamu bisa menemukan **Singgasana Surga** di Gunung Ashenfang sebelum malam tiba! 🌄🔥

