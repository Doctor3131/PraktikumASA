<!-- PREVIEW CTRL SHIFT V -->

# ⚽ **Analisis Gol Pemain: Seberapa Tajam Seorang Penyerang?** 🎯

## 📖 **Latar Belakang**
Seorang **analis sepak bola** sedang meneliti performa **seorang penyerang** dalam sebuah liga.  

Setiap musim, data jumlah gol yang dicetak oleh pemain direpresentasikan dalam **bilangan N** berbentuk **biner dengan panjang 32 bit**.  

- **Bit bernilai `1`** → Pemain mencetak **gol** dalam pertandingan tertentu.  
- **Bit bernilai `0`** → Pemain **tidak mencetak gol** di pertandingan tersebut.  

Tugas kita adalah **menghitung jumlah pertandingan di mana pemain tersebut mencetak gol**.  

> Apakah pemain ini seorang **raja gol** atau hanya sekadar **striker biasa**? Mari kita analisis! 📊

---

## 📥 **Format Input**
Sebuah **bilangan bulat tak bertanda** `N` yang merepresentasikan statistik musim dalam format **32-bit**.

---

## 📤 **Format Output**
Sebuah **bilangan bulat** yang menyatakan **jumlah pertandingan** di mana pemain mencetak gol (**jumlah bit `1` dalam representasi biner dari `N`**).

---

## 📌 **Contoh Input & Output**

### 🎯 **Contoh 1**
#### **Input**
7
#### **Representasi Biner**
00000000000000000000000000000111
#### **Output**
3
📌 **Penjelasan:**  
Bilangan **7** dalam biner adalah **00000000000000000000000000000111**.  
Ada **tiga** bit `1`, sehingga pemain mencetak gol dalam **3 pertandingan**.

---

### 🎯 **Contoh 2**
#### **Input**
9
#### **Representasi Biner**
00000000000000000000000000001001
#### **Output**
📌 **Penjelasan:**  
Bilangan **9** dalam biner adalah **00000000000000000000000000001001**.  
Ada **dua** bit `1`, berarti pemain mencetak gol dalam **2 pertandingan**.

---

## 🔍 **Strategi Penyelesaian**
Untuk menemukan jumlah pertandingan di mana pemain mencetak gol:
1. **Konversi bilangan N ke biner**.
2. **Hitung jumlah bit `1`** dalam representasi biner tersebut.
3. **Cetak hasilnya** sebagai jumlah pertandingan di mana pemain mencetak gol.

---

## 🏆 **Tantangan untukmu!**
Bisakah kamu **menghitung jumlah gol pemain ini dengan efisien**? 🚀  
Coba pikirkan bagaimana caranya **menggunakan operasi bit** untuk menyelesaikan masalah ini dengan cepat! 🔥  

💡 **"Gol tercipta bukan hanya dari peluang, tapi dari strategi yang matang!"** ⚽  
