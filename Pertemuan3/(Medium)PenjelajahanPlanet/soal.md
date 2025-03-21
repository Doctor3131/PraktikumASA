# 🚀 Misi Eksplorasi Planet Zygma 🪐

## Latar Belakang

Tim ekspedisi luar angkasa dari Galactic Exploration Union (GEU) sedang melaksanakan misi eksplorasi di Planet Zygma, sebuah planet misterius dengan medan yang ekstrem. Untuk menjamin keselamatan dan efisiensi misi, tim perlu menemukan jalur ekspedisi terbaik yang meminimalkan perubahan ketinggian yang drastis pada kendaraan penelitian mereka.

## 🧩 Permasalahan

Tim GEU telah memetakan N titik ketinggian yang merepresentasikan jalur potensial yang bisa dilalui. Tantangan mereka adalah menemukan dua titik dengan **selisih ketinggian terkecil** di jalur tersebut.

Karena banyaknya data yang dikumpulkan, tim menggunakan algoritma **Divide and Conquer** untuk menemukan solusi secara efisien.

**Tantangan Tambahan**: Jika ada lebih dari satu pasang titik yang memiliki selisih terkecil, sistem harus mencari pasangan dengan **indeks terkecil** dalam daftar.

## 📥 Format Input

- Baris pertama berisi bilangan bulat N (2 ≤ N ≤ 10⁵), menyatakan jumlah titik ketinggian
- Baris kedua berisi N bilangan bulat yang dipisahkan oleh spasi, menyatakan ketinggian setiap titik

## 📊 Batasan

- Jumlah titik ketinggian: 2 ≤ N ≤ 10⁵
- Nilai ketinggian: -10⁹ ≤ A[i] ≤ 10⁹ (bisa positif, negatif, atau nol)

## 📤 Format Output

Cetak dua bilangan bulat:
1. Selisih ketinggian terkecil di antara dua titik
2. Indeks terkecil dari pasangan yang memiliki selisih tersebut (indeks dimulai dari 1)

## 📋 Contoh

### Contoh 1

**Input:**
```
6
10 15 12 18 19 21
```

**Output:**
```
1 4
```

**Penjelasan:**
- Ketinggian: [10, 15, 12, 18, 19, 21]
- Pasangan dengan selisih terkecil:
  - (18, 19) dengan selisih 1, indeks 4 dan 5
- Jadi output adalah: 1 (selisih) dan 4 (indeks terkecil)

### Contoh 2

**Input:**
```
4
-50 -47 -45 -40
```

**Output:**
```
2 2
```

**Penjelasan:**
- Ketinggian: [-50, -47, -45, -40]
- Pasangan dengan selisih terkecil:
  - (-47, -45) dengan selisih 2, indeks 2 dan 3
- Jadi output adalah: 2 (selisih) dan 2 (indeks terkecil)

### Contoh 3

**Input:**
```
3
-1000000000 0 1000000000
```

**Output:**
```
1000000000 1
```

**Penjelasan:**
- Ketinggian: [-1000000000, 0, 1000000000]
- Pasangan dengan selisih terkecil:
  - (-1000000000, 0) dengan selisih 1000000000, indeks 1 dan 2
  - (0, 1000000000) dengan selisih 1000000000, indeks 2 dan 3
- Karena keduanya memiliki selisih yang sama, pilih yang indeksnya lebih kecil
- Jadi output adalah: 1000000000 (selisih) dan 1 (indeks terkecil)

## 🧠 Analisis Algoritma

Solusi menggunakan pendekatan **Divide and Conquer**:
1. Bagi array ketinggian menjadi dua bagian
2. Cari selisih terkecil pada bagian kiri dan kanan secara rekursif
3. Cari kemungkinan pasangan yang melewati garis tengah
4. Bandingkan ketiga hasil dan pilih yang memiliki selisih terkecil
5. Jika ada beberapa pasangan dengan selisih sama, pilih yang indeksnya terkecil

## 💻 Kompleksitas

- **Time Complexity**: O(N log² N) - karena kita melakukan divide and conquer dengan penggabungan yang memerlukan pengurutan
- **Space Complexity**: O(N) - untuk menyimpan array tambahan

## 🛸 Kesimpulan

Dengan menemukan jalur dengan perubahan ketinggian minimal, tim GEU dapat memastikan kendaraan ekspedisi mereka beroperasi dengan aman di medan ekstrem Planet Zygma, meminimalkan risiko kerusakan, dan meningkatkan efisiensi misi penjelajahan.