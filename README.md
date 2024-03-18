<h1 align="center">Tugas Kecil 2 IF2211 Strategi Algoritma</h1>
<h3 align="center">Membangun Kurva Bézier dengan</p>
<h3 align="center">Algoritma Titik Tengah berbasis Divide and Conquer</p>

## Table of Contents

- [Overview](#overview)
- [Abstraction](#abstraction)
- [Built With](#built-with)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Links](#links)


## Overview
Anggota Tim :
- 13522117 - Mesach Harmasendo
- 13522047 - Farel Winalda

<p>Our Lecturer : Dr. Ir. Rinaldi Munir, M.T.</p>

Tujuan pembuatan projek ini:
- Mengimplementasikan algoritma Divide and Conquer dalam pembuatan Kurva Bézier
- Mengimplementasikan algoritma BruteForce dalam pembuatan Kurva Bézier
- Membuat program pembuatan Kurva Bézier dengan n titik kontrol
- Membuat interface pengguna yang menerima masukan pengguna

## Abstraction

Projek ini dibuat untuk memenuhi spesifikasi dari Tugas Kecil 2 - IF2211 Strategi Algoritma yaitu dengan membuat program untuk membuat Kurva Bézier dengan menggunakan Algoritma Divide and Conquer. Program pada projek ini dibuat dengan menggunakan bahasa pemrograman python. Pada program ini, terdapat interface pengguna yang dibuat dengan menggunakan GUI dengan library tkinter dan pembuatan serta penganimasian Kurva Bézier dengan menggunakan library matplotlib.

Pada program ini, pengguna akan diminta untuk memberikan masukan berupa titik kontrol ( 3 atau n titik kontrol) dan jumlah iterasi titik yang diberikan. Lalu, pengguna diminta untuk memilih 2 opsi pembuatan kurva, yaitu dengan menggunakan algoritma Divide and Conquer atau dengan BruteForce. Lalu akan dibentuk 2 Kurva Bézier, tanpa animasi dan dengan animasi. Lalu, akan ditampilkan pula output berupa lama eksekusi dari program sesuai dengan algoritma yang dipilih.

## Built With

- [Python](https://www.python.org/)
- [TkInter](https://docs.python.org/3/library/tkinter.html)
- [Matplotlib](https://matplotlib.org/)

## Prerequisites

Untuk menjalankan program ini, diperlukan beberapa prasyarat:
- `Python` : Python digunakan dalam semua bagian pembuatan program ini dan versi Python yang digunakan adalah versi 3

## Installation

Langkah-langkah instalasi projek ini:

1. Clone repository :
```shell
git clone https://github.com/Otzzu/tucil-2-stima
```

2. Masuk ke source file :
```shell
cd  src
```

3. Memilih menjalankan 3 titik kontrol atau n titik kontrol :
n titik kontrol
```shell
python main_n.py
```
3 titik kontrol
```shell
python main_3.py
```

Maka, program sudah bias digunakan dengan masukan sesuai format yang dicontohkan

## Usage

Langkah-langkah dalam penggunaan program n titik kontrol:
1. Memasukkan input titik kontrol
<img src="img/n point input control point.png" alt="Input n titik kontrol" width="300" height="200"/>

2. Memasukkan input jumlah iterasi
<img src="img/n point input iterasi.png" alt="Input jumlah iterasi" width="300" height="200"/>

3. Memilih antara algoritma Divide and Conquer atau BruteForce
    - Divide and Conquer
    <img src="img/n point dnc.png" alt="DNC n input" width="300" height="200"/>
    - BruteForce
    <img src="img/n point bf.png" alt="BF n input" width="300" height="200"/>

Hal serupa juga digunakan dalam langkah-langkah penggunaan program 3 titik kontrol:
- Contoh penggunaan program 3 titik kontrol
    - Divide and Conqier
    <img src="img/3 point dnc.png" alt="DNC 3 input" width="300" height="200"/>
    - BruteForce
    <img src="img/3 point bf.png" alt="BF 3 input" width="300" height="200"/>

## Links

Kontributor dibalik pengerjaan projek ini:
- [@Otzzu](https://github.com/Otzzu)
- [@FarelW](https://github.com/FarelW)

