<!-- PREVIEW CTRL SHIFT V -->

# 🏰 **KEKUATAN DALAM JUMLAH** ⚔️

## 📖 **Latar Belakang**
Swain, **penguasa kerajaan Noxus**, berdiri di atas menaranya yang megah, mengawasi kerajaannya dengan penuh kewaspadaan.  

Di bawah, jalanan **dipenuhi berbagai macam penduduk Noxus** — prajurit, pedagang, cendekiawan, dan para buangan.  
Swain tahu bahwa **kekuatan berasal dari kendali**, tetapi jika **satu golongan menjadi terlalu dominan**, mereka **mungkin menantang kekuasaannya**.  

> _"Kekuatan ada dalam jumlah,"_ bisik mereka di kegelapan. 🌑  

Swain harus segera bertindak!  
Dia memerintahkan **para penasihat kepercayaannya** untuk **menganalisis** situasi.  

Menghitung satu per satu **tidaklah efisien**, dan **waktu bukanlah kemewahan** yang dimilikinya.  
Sebagai gantinya, mereka menyusun strategi menggunakan **Divide and Conquer**.  

Sebagai **penasihat kepercayaannya**, tugasmu adalah **menemukan golongan mayoritas** di antara penduduk Noxus sebelum semuanya terlambat!  

---

## 🛠️ **Tugas**
Diberikan **N penduduk Noxus**, setiap penduduk memiliki **golongan tertentu**.  
Temukan **golongan mayoritas**, yaitu golongan yang **muncul lebih dari atau sama dengan N/2 kali**.  

Jika tidak ada golongan yang memenuhi syarat, maka **Swain tidak perlu khawatir**, dan kita akan mengembalikan **-1**.  

> Gunakan **Divide and Conquer** untuk menyelesaikan masalah ini dengan **efisien**!

---

## 📥 **Format Input**
1. **Baris pertama** berisi bilangan bulat **N** _(jumlah penduduk Noxus)_.
2. **Baris kedua** berisi **N bilangan bulat** yang merepresentasikan **golongan setiap penduduk**.

---

## 📤 **Format Output**
Cetak **satu bilangan bulat** yang menunjukkan **golongan penduduk Noxus** yang memiliki populasi **mayoritas (≥ N/2)**.  

Jika **tidak ada**, kembalikan **"-1"**.

---

## 📌 **Contoh Input & Output**

### 🎯 **Contoh 1**
#### **Input**
7 3 3 4 2 3 3 3
#### **Output**
3
📌 **Penjelasan:**  
Golongan **3** muncul **4 kali** dari **7**, yang lebih dari atau sama dengan **N/2** → **Mayoritas!**

---

### 🎯 **Contoh 2**
#### **Input**
6 1 2 3 4 5 6
#### **Output**
-1
📌 **Penjelasan:**  
Tidak ada **golongan** yang memiliki jumlah **≥ N/2**. Tidak ada ancaman bagi Swain!

---

## 🔍 **Strategi Penyelesaian**
Karena **N kecil (≤ 12)**, kita dapat menggunakan strategi **Divide and Conquer**:  
1. **Bagikan array menjadi dua bagian** hingga hanya tersisa satu elemen.
2. **Tentukan mayoritas dari setiap bagian**.
3. **Gabungkan hasilnya** untuk menemukan mayoritas keseluruhan.

---

## 🏆 **Tantangan untukmu!**
Dapatkah kamu **mengimplementasikan algoritma Divide and Conquer** untuk membantu Swain mempertahankan **kekuatannya** di Noxus?  

⚔️ **Pilih dengan bijak, penasihat!** Karena di Noxus, **hanya yang kuat yang bertahan!** 🔥  

