# Menghitung Inversi Daftar Nilai

## Latar Belakang

Anya Forger sedang belajar di Eden College dan ingin menjadi murid terbaik untuk mendapatkan Stella ⭐!

Setiap minggu, Eden College mengumumkan daftar nilai ujian murid-muridnya. Namun, semakin tidak teratur daftar tersebut, semakin sulit bagi Damian Desmond untuk menerima hasilnya!

Anya ingin mengetahui seberapa tidak teratur daftar nilai ujian. Ia mendefinisikan ketidakteraturan sebagai jumlah inversi dalam daftar nilai.

## Definisi Inversi

Inversi terjadi jika ada dua nilai (i, j) dengan i < j, tetapi nilai[i] > nilai[j].

Dengan kata lain, inversi terjadi ketika ada nilai yang lebih besar yang muncul sebelum nilai yang lebih kecil dalam daftar.

## Tugas

Bantu Anya menghitung jumlah inversi dalam daftar nilai ujian teman-temannya!

## Format Input

- Baris pertama berisi bilangan bulat N (1 ≤ N ≤ 100000), jumlah murid Eden College.
- Baris kedua berisi N bilangan bulat yang menunjukkan nilai ujian murid-murid dalam urutan yang diumumkan oleh sekolah. (1 ≤ nilai ≤ 100000)

## Batasan

- 1 ≤ N ≤ 100000
- 1 ≤ nilai ≤ 100000

## Format Output

Cetak satu bilangan bulat, yaitu jumlah inversi dalam daftar nilai.

## Contoh 1

### Input
```
5
2 4 1 3 5
```

### Output
```
3
```

### Penjelasan
Daftar nilai murid: [2, 4, 1, 3, 5]
Terdapat 3 inversi:
- (4,1) → 4 lebih dulu tetapi lebih besar dari 1
- (2,1) → 2 lebih dulu tetapi lebih besar dari 1
- (4,3) → 4 lebih dulu tetapi lebih besar dari 3

## Contoh 2

### Input
```
4
10 20 30 40
```

### Output
```
0
```

### Penjelasan
Daftar nilai murid: [10, 20, 30, 40]
Tidak terdapat inversi karena daftar nilai sudah terurut dari kecil ke besar.