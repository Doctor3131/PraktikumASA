# Pahlawan dan Menara Penjaga

## Deskripsi Masalah

Di sebuah dunia fantasi, ada sebuah menara yang dijaga oleh sejumlah penjaga. Setiap lantai menara dijaga oleh satu penjaga yang lebih kuat dari penjaga di lantai bawahnya. Seorang pahlawan harus mencapai puncak menara, tetapi untuk melakukannya, ia harus mengalahkan setiap penjaga secara berurutan dari lantai pertama hingga lantai terakhir.

Diberikan sebuah bilangan bulat P yang menyatakan kekuatan awal pahlawan dan sebuah array G berisi N bilangan bulat yang menyatakan kekuatan penjaga di setiap lantai (dari lantai pertama hingga lantai ke-N). Jika pahlawan memiliki kekuatan lebih besar atau sama dengan kekuatan penjaga di lantai tertentu, ia dapat mengalahkan penjaga tersebut dan menambahkan kekuatan penjaga ke kekuatannya sendiri. Jika tidak, pahlawan akan terhenti dan tidak bisa melanjutkan ke lantai berikutnya.

Buatlah program yang menentukan apakah pahlawan bisa mencapai puncak menara atau tidak dengan menggunakan algoritma decrease and conquer.

## Format Input

* Baris pertama berisi dua bilangan bulat N dan P, dipisahkan oleh spasi.
* Baris kedua berisi N bilangan bulat G[i] yang menyatakan kekuatan penjaga di tiap lantai.

## Batasan (Constraints)

* 1 <= N <= 100000
* 1 <= P, G[i] <= 10^9

## Format Output

* Cetak "YES" jika pahlawan dapat mencapai puncak menara.
* Cetak "NO" jika pahlawan terhenti di tengah jalan.

## Contoh Input dan Output

### Contoh 1

**Input:**
```
2 1
2 1
```

**Output:**
```
NO
```

### Contoh 2

**Input:**
```
4 4
2 3 5 7
```

**Output:**
```
YES
```

## Penjelasan

Pada contoh pertama, pahlawan memiliki kekuatan awal 1, yang tidak cukup untuk mengalahkan penjaga pertama dengan kekuatan 2, sehingga pahlawan terhenti dan tidak bisa mencapai puncak menara.

Pada contoh kedua, pahlawan memiliki kekuatan awal 4. Ia dapat mengalahkan penjaga pertama (kekuatan 2), sehingga kekuatannya menjadi 4+2=6. Kemudian ia dapat mengalahkan penjaga kedua (kekuatan 3), sehingga kekuatannya menjadi 6+3=9. Kemudian ia dapat mengalahkan penjaga ketiga (kekuatan 5), sehingga kekuatannya menjadi 9+5=14. Akhirnya, ia dapat mengalahkan penjaga keempat (kekuatan 7), sehingga pahlawan berhasil mencapai puncak menara.