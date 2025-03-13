# 🔎 **Mencari Substring Baik Terpanjang** 🔍

## 📖 **Pendahuluan**
Di dunia kriptografi kuno, terdapat **kode rahasia** yang hanya bisa dipecahkan jika sebuah **substring** memenuhi kriteria tertentu. Sebuah substring dikatakan **baik** jika dalam string `s`, setiap **huruf alfabet** yang ada dalam substring muncul dalam **huruf besar dan kecil**.  

**Contoh:**  
✅ **"abABB"** → **Benar**, karena `'A'` & `'a'`, `'B'` & `'b'` muncul bersama-sama.  
❌ **"abA"** → **Salah**, karena `'b'` muncul, tetapi `'B'` tidak ada.  

Tugas kita adalah **menemukan substring terpanjang yang baik** dalam `s`.  
Jika ada beberapa substring dengan panjang yang sama, **ambil yang pertama muncul**.  
Jika tidak ada substring yang valid, **kembalikan string kosong** (`""`).

---

## 📥 **Format Input**
- Sebuah **string** `s` dengan panjang **1 ≤ s.length ≤ 100`.

---

## 📤 **Format Output**
- Sebuah **substring** yang merupakan substring **baik** terpanjang.
- Jika tidak ditemukan, kembalikan **string kosong** (`""`).

---

## 📌 **Contoh Input & Output**

### 🎯 **Contoh 1**
#### **Input**
YazaAay
#### **Output**
aAa
📌 **Penjelasan:**  
Substring **"aAa"** adalah substring yang baik karena **huruf 'a' dan 'A' muncul** berpasangan.

---

### 🎯 **Contoh 2**
#### **Input**
Bb
#### **Output**
Bb
📌 **Penjelasan:**  
Substring **"Bb"** adalah substring yang baik karena **'B' dan 'b' muncul bersama-sama**.

---

## 🔍 **Bagaimana Menyelesaikan Masalah Ini?**
1. **Periksa setiap substring dari string `s`**.
2. **Cek apakah substring itu valid** (semua huruf muncul dalam kapital & non-kapital).
3. **Cari substring terpanjang** dan simpan posisi kemunculan pertama.
4. **Cetak substring tersebut** atau **kembalikan string kosong (`""`)** jika tidak ada yang valid.

---

## 🚀 **Tantangan untukmu!**
Bisakah kamu membuat **algoritma yang optimal** untuk menyelesaikan masalah ini dalam **waktu yang efisien**? ⏳  

🧩 **"Hanya kombinasi huruf yang sempurna yang dapat membuka rahasia ini!"** 🔐  
