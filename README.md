# latihan-deri-ar
"Membuat program sederhana pada pyhton menggunakan "List"
A. Algoritma Program
Start

Inisialisasi: Buat sebuah daftar kosong data_mahasiswa untuk menyimpan data mahasiswa.

Perulangan:

-Tampilkan pesan: "Masukkan data mahasiswa:"

-Input:

=> nama → masukkan nama mahasiswa.

=> nim → masukkan NIM mahasiswa.

=> nilai_tugas → masukkan nilai tugas.

=> nilai_uts → masukkan nilai UTS.

=> nilai_uas → masukkan nilai UAS.

Hitung nilai akhir:
Gunakan rumus:

nilai_akhir=(nilai_tugas×0.3)+(nilai_uts×0.35)+(nilai_uas×0.35)

Simpan data ke daftar data_mahasiswa:
Data yang disimpan mencakup: nama, nim, nilai_tugas, nilai_uts, nilai_uas, dan nilai_akhir.

Tanya pengguna:
=> "Tambah data lagi (y/t)?"

=> Jika jawabannya "y", ulangi langkah input data.

=> Jika jawabannya "t", keluar dari perulangan.

Tampilkan data mahasiswa dalam bentuk tabel:
=> Cetak header tabel: No | Nama | NIM | Tugas | UTS | UAS | Akhir.

=> Gunakan perulangan untuk mencetak data dari daftar data_mahasiswa.

End
B. Gambar Flowchart Program
Flowchart 6 drawio

C. Menampilkan Penjelasan Program Yang telah dibuat menggunakan program "Perulangan" dan "List"
Gambar Program

Berikut Penjelasan Programnya

Fungsi hitung_nilai_akhir
image

Fungsi ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan bobot: Tugas: 30%, UTS: 35%, UAS: 35%.

Fungsi menerima tiga parameter: tugas, uts, dan uas, lalu mengembalikan nilai akhir yang dibulatkan hingga dua desimal.

Variabel data_mahasiswa
image

Sebuah list kosong yang digunakan untuk menyimpan data semua mahasiswa. Setiap data mahasiswa akan dimasukkan ke dalam list ini dalam bentuk dictionary.

Perulangan untuk Input Data
image

Program memasukkan data mahasiswa satu per satu, termasuk:

=> Nama (nama),

=> NIM (nim),

=> Nilai tugas (nilai_tugas),

=> Nilai UTS (nilai_uts),

=> Nilai UAS (nilai_uas).

Input untuk nilai tugas, UTS, dan UAS dikonversi ke tipe float agar bisa dilakukan perhitungan matematika.

Hitung Nilai Akhir
image

Nilai akhir dihitung menggunakan fungsi hitung_nilai_akhir.

Simpan Data ke dalam List
image

Data mahasiswa disimpan dalam dictionary dengan struktur:

=> Nama: Nama mahasiswa,

=> NIM: NIM mahasiswa,

=> Tugas: Nilai tugas,

=> UTS: Nilai UTS,

=> UAS: Nilai UAS,

=> Akhir: Nilai akhir.

Dictionary tersebut ditambahkan ke dalam list data_mahasiswa.

Periksa Input Tambahan
image

Program menanyakan apakah pengguna ingin menambahkan data lagi:

=> Jika pengguna menjawab "y", program mengulangi langkah input data.

=> Jika pengguna menjawab selain "y" (misalnya "t"), program keluar dari perulangan.

Cetak Tabel Data Mahasiswa
image

Program mencetak header tabel dengan kolom:

=> No: Nomor urut,

=> Nama: Nama mahasiswa,

=> NIM: NIM mahasiswa,

=> Tugas: Nilai tugas,

=> UTS: Nilai UTS,

=> UAS: Nilai UAS,

=> Akhir: Nilai akhir.

=> Garis "=" digunakan untuk membuat tabel lebih rapi.

Tampilkan Data Mahasiswa
image

Menggunakan for loop untuk mencetak data setiap mahasiswa dari list data_mahasiswa:

=> i: Nomor urut mahasiswa.

=> mahasiswa: Dictionary berisi data mahasiswa.

Data ditampilkan sesuai dengan kolom di header tabel.

Akhiri Program
Setelah semua data dicetak, program selesai.

D. Hasil Program yang telah dijalankan dengan mengklik "Run"
