# Soal: Menemukan Koin Palsu dengan Decrease and Conquer

## Deskripsi Masalah
Tersembunyi di dalam rimba luas Ixtal, terdapat kerajaan Ixaocan. Salah satu putrinya, Qiyana, adalah seorang putri yang bangga dan angkuh, yang hanya menuntut emas terbaik untuk hiasan kepala upacaranya. Ketika para pengrajin kerajaan mempersembahkan sebuah peti berisi *N* koin emas, dia mencibir.

> "Apa kalian menganggapku bodoh? Salah satu dari koin ini terasa... aneh."

Para penasihat ragu — siapa yang berani meragukan intuisi sang putri? Untuk membuktikan keunggulannya, Qiyana meraih **Timbangan Ixtal**, sebuah timbangan suci yang hanya dapat **membandingkan berat**, bukan mengukurnya.

Qiyana adalah putri yang tidak sabaran. Menimbang koin satu per satu akan memakan terlalu banyak waktu. Untungnya, ada sebuah metode di mana setiap langkah akan mengurangi jumlah koin yang dicurigai, hingga akhirnya koin palsu ditemukan.

Tugas Anda adalah membuat algoritma **Decrease and Conquer** untuk membantu Qiyana menemukan koin palsu dengan efisien.

## **Format Input**
- Baris pertama berisi bilangan bulat *N* yang menunjukkan jumlah koin.
- Baris kedua berisi *N* bilangan bulat di mana *A[i]* menunjukkan berat koin ke-*i*.

## **Batasan**
- 1 \leq *N* \leq 20
- 0 \leq *A[i]* \leq 20
- Hanya ada satu koin yang lebih ringan dari yang lain.

## **Format Output**
Sebuah bilangan bulat berupa indeks koin palsu dalam **zero-based index**.

## **Contoh**
### **Input 1:**
```
4
10 10 9 10
```
### **Output 1:**
```
2
```
**Penjelasan:** Koin palsu berada di indeks ke-2 (zero-based index).

### **Input 2:**
```
7
10 10 10 9 10 10 10
```
### **Output 2:**
```
3
```
**Penjelasan:** Koin palsu berada di indeks ke-3 (zero-based index).

---

**Petunjuk:** Gunakan metode **Decrease and Conquer** dengan cara membandingkan bobot dua kelompok koin dan mengabaikan setengah dari kandidat setiap iterasi.

