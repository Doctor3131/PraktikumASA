# 🎮 Game Kesukaan Pai - Power Creep Rail 🚂🔥

## 📜 Deskripsi

Pada game **Power Creep Rail**, ada event spesial bernama **Apocalyptic Black** yang memberikan hadiah harian kepada pemain yang mendapatkan skor tinggi! 💥 Hadiah dalam event ini di-*reset* setiap hari, jadi pemain harus terus menyelesaikan tantangan harian untuk mengumpulkan hadiah sebanyak mungkin! 🎁

Pai, seorang gamer sejati, tentu tidak mau ketinggalan! 💪 Dia telah bermain selama **K** hari dan ingin tahu berapa banyak hadiah yang telah ia kumpulkan dari event ini. Bisa bantu hitung? 🤔

---

## 📥 Format Masukan
1. **Baris pertama** berisi dua bilangan bulat **N** dan **K**
   - **N** → Jumlah hadiah yang tersedia per hari *(1 ≤ N ≤ 100000)*
   - **K** → Jumlah hari Pai bermain *(1 ≤ K ≤ 100000)*

2. **Baris kedua** berisi **N** bilangan bulat **A₁, A₂, ..., Aₙ** yang merupakan skor minimal untuk mendapatkan hadiah tertentu.
   - *(1 ≤ Aᵢ ≤ 10000)*

3. **Baris ketiga** berisi **K** bilangan bulat **S₁, S₂, ..., Sₖ** yang merupakan skor harian Pai.
   - *(1 ≤ Sᵢ ≤ 10000)*

---

## 📤 Format Keluaran
Sebuah bilangan bulat yang menunjukkan total hadiah yang didapat Pai selama **K** hari bermain! 🏆

---

## 📌 Contoh Masukan 1
```
5 4
3 10 8 6 11
9 11 3 11
```

## 📌 Contoh Keluaran 1
```
14
```

---

## 📖 Penjelasan Contoh

| Hari | Skor Pai | Hadiah yang Diterima | Total Hadiah |
|------|---------|----------------------|--------------|
| 1    | 9       | 3 hadiah 🎁🎁🎁       | 3            |
| 2    | 11      | 5 hadiah 🎁🎁🎁🎁🎁     | 8            |
| 3    | 3       | 1 hadiah 🎁          | 9            |
| 4    | 11      | 5 hadiah 🎁🎁🎁🎁🎁     | 14           |

Jadi, total hadiah yang dikumpulkan oleh Pai adalah **14**! 🎉🎉

---

## 🧠 Strategi Penyelesaian
Untuk menghitung jumlah hadiah yang didapat Pai:
1. Urutkan daftar skor hadiah **A** secara **ascending**.
2. Untuk setiap skor **S** yang didapat Pai:
   - Hitung jumlah elemen dalam **A** yang ≤ **S** (bisa dengan *binary search* untuk efisiensi).
   - Tambahkan jumlah ini ke total hadiah Pai.

⏳ Dengan cara ini, kita bisa menyelesaikan masalah dalam **O(N log N + K log N)** menggunakan **binary search**, sehingga tetap cepat untuk batasan maksimum!

---

## 🏁 Yuk, Tantang Skor Terbaikmu!
Sekarang, apakah kamu bisa membantu Pai mengoptimalkan hadiahnya? 💪🎮

> **"Gotta catch 'em all... hadiah!"** 🎁🔥

