<!-- PREVIEW CTRL SHIFT V -->

# 🔍 Quantum-Eye: Menangkap Bayangan di Elysium

## 📖 Latar Belakang
Di sebuah pemerintahan futuristik bernama **Elysium**, telah terjadi pencurian **chip penting** yang dapat menghancurkan semua manusia Cyborg! 🤖🔥  

Beruntungnya, kota ini diawasi oleh **Quantum-Eye**, sistem pengawasan canggih yang mencatat setiap individu yang masuk dan keluar dari lokasi tertentu.  

Namun, ada satu masalah...  
Quantum-Eye **tidak merekam identitas langsung seseorang**. Sebagai gantinya, ia hanya mencatat **log kedatangan**, berupa daftar angka unik yang **disusun berdasarkan waktu (menit) mereka masuk**.  

Kini, seorang **saksi mata** telah memberikan informasi identitas **pelaku yang dicurigai**!  
Tugas kita adalah mencari tahu **menit awal** dan **menit akhir** kedatangan mereka dalam bentuk **indeks** untuk segera ditindaklanjuti oleh **divisi penyidik**.  

Apakah kita bisa menemukannya tepat waktu?  
Ataukah Quantum-Eye hanya akan memberimu **"-1 -1"**, tanda bahwa bayangan itu telah menghilang selamanya? 👀💀  

---

## 📥 Format Input
1. **Baris pertama** berisi dua bilangan bulat **n** _(jumlah individu dalam log)_ dan **k** _(identitas yang dicari)_.
2. **Baris kedua** berisi **array angka unik** yang telah **terurut naik**, mewakili **ID individu** yang masuk ke lokasi tertentu.

---

## 📤 Format Output
Cetak **dua bilangan bulat** yang menunjukkan **index pertama** dan **index terakhir** kemunculan identitas yang dicari.  

- **Index dimulai dari 1.**
- Jika tidak ditemukan, cetak **"-1 -1"**.

---

## 📌 Contoh Input & Output

### 🎯 Contoh 1
#### **Input**
6 10 8 8 9 9 10 10
#### **Output**
5 6

---

### 🎯 Contoh 2
#### **Input**
1 2 2
#### **Output**
1 1

---

### 🎯 Contoh 3
#### **Input**
10 21 16 16 17 18 19 20 20 22 22 30
#### **Output**
-1 -1

---

## 🛠️ Penyelesaian dengan **Binary Search**
Karena log **terurut naik**, pencarian harus dilakukan dengan cara **efisien**.  
Gunakan **Binary Search (O(log N))** untuk mencari **index pertama dan terakhir** dari identitas yang dicari.

### 🔍 **Langkah-langkah Algoritma:**
1. **Gunakan Binary Search** untuk menemukan **index pertama** dari identitas yang dicari.
2. **Gunakan Binary Search** lagi untuk menemukan **index terakhir**.
3. Jika identitas tidak ditemukan, kembalikan **"-1 -1"**.

---

## 🚀 Tantangan untukmu!
Bisakah kamu mengimplementasikan **algoritma Binary Search** untuk menyelesaikan masalah ini **dengan efisien**?  
Selamat mencari **bayangan** di Quantum-Eye! 🕵️‍♂️💽  

Atau... mungkinkah sang pencuri sudah **menghapus jejaknya selamanya**? 🕶️❌
