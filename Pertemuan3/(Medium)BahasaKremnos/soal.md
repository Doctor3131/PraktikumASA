# 🏛️ Problema Bahasa Kremnos yang Hilang 🏛️

## Latar Belakang

Phainon, seorang murid berbakat, diberi tugas menarik oleh profesor Anaxagoras mengenai bahasa kuno yang telah hilang - bahasa Kremnos. Bahasa ini memiliki aturan kesetaraan string yang unik dan misterius.

## 🧩 Permasalahan

Tentukan apakah dua string dengan panjang yang sama dapat dianggap ekuivalen dalam bahasa Kremnos, berdasarkan aturan-aturan berikut:

### Aturan Ekuivalensi Kremnos:

1. **Jika panjang string ganjil:**
   - Dua string ekuivalen jika dan hanya jika keduanya identik

2. **Jika panjang string genap:**
   - Dua string ekuivalen jika salah satu kondisi berikut terpenuhi:
     - Keduanya identik, ATAU
     - Jika string A dibagi menjadi A₁ dan A₂, dan string B dibagi menjadi B₁ dan B₂, maka:
       - A₁ ekuivalen dengan B₁ DAN A₂ ekuivalen dengan B₂, ATAU
       - A₁ ekuivalen dengan B₂ DAN A₂ ekuivalen dengan B₁

## 📥 Format Input

Dua string yang ingin dicek ekuivalensinya, masing-masing dalam baris terpisah. Dijamin kedua string memiliki panjang yang sama.

## 📤 Format Output

- `YA` jika dua string ekuivalen
- `TIDAK` jika dua string tidak ekuivalen

## 📋 Contoh

### Contoh 1

**Input:**
```
baaa
aaab
```

**Output:**
```
YA
```

**Penjelasan:**
- Kedua string memiliki panjang 4 (genap)
- String dibagi menjadi dua:
  - 'baaa' → 'ba' dan 'aa'
  - 'aaab' → 'aa' dan 'ab'
- Memeriksa kondisi kedua:
  - 'ba' ekuivalen dengan 'ab'? 
    - Keduanya memiliki panjang 2 (genap)
    - Tidak identik
    - Dibagi lagi: 'b'+'a' dan 'a'+'b'
    - 'b' ekuivalen dengan 'b'? Ya (identik)
    - 'a' ekuivalen dengan 'a'? Ya (identik)
    - Jadi 'ba' ekuivalen dengan 'ab'
  - 'aa' ekuivalen dengan 'aa'? Ya (identik)
- Jadi kedua string ekuivalen

### Contoh 2

**Input:**
```
bbab
aabb
```

**Output:**
```
TIDAK
```

## 🧠 Tantangan

Anda perlu mengimplementasikan solusi rekursif untuk masalah ini, karena definisi ekuivalensi bergantung pada ekuivalensi dari bagian-bagian yang lebih kecil.

Selamat memecahkan misteri bahasa kuno Kremnos! 🏺📜