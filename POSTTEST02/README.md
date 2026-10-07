Sistem Manajemen Toko Skincare (Skin Studio)
Deskripsi Program

Program ini adalah simulasi pengelolaan toko skincare yang dibuat dengan Python menggunakan konsep Pemrograman Berorientasi Objek. Program dapat mengelola data produk beserta stoknya, mencatat data pelanggan, memproses transaksi pembelian, dan menyimpan riwayat transaksi untuk setiap cabang toko. Pada posttest ini, program dikembangkan dengan menerapkan relasi UML (asosiasi, agregasi, dan komposisi) serta inheritance.

Struktur Kelas

Program terdiri dari tujuh kelas. ProdukSkincare adalah kelas utama yang menyimpan data produk seperti id, nama, jenis, harga, dan stok. ProdukSunscreen dan ProdukSerum adalah kelas turunan dari ProdukSkincare. Pelanggan menyimpan data pelanggan beserta poinnya. Transaksi mencatat satu pembelian produk. RiwayatTransaksi menyimpan daftar transaksi milik sebuah toko. TokoSkincare adalah kelas yang mewakili satu cabang toko dan mengatur produk serta transaksinya.

Relasi UML
Asosiasi

Asosiasi diterapkan pada kelas Transaksi yang berhubungan dengan kelas ProdukSkincare dan Pelanggan. Objek Transaksi menyimpan referensi ke produk yang dibeli dan pelanggan yang membeli. Produk dan pelanggan adalah objek yang berdiri sendiri, sehingga tetap ada walaupun transaksinya tidak ada.

Agregasi

Agregasi diterapkan pada hubungan antara TokoSkincare dan ProdukSkincare. Produk dibuat di luar toko, kemudian dimasukkan ke dalam toko melalui method tambah_produk(). Ketika produk dihapus dari toko dengan hapus_produk(), objek produknya tidak ikut hilang dan masih bisa dipakai, misalnya oleh cabang lain. Hal inilah yang membedakan agregasi dari komposisi.

Komposisi

Komposisi diterapkan pada hubungan antara TokoSkincare dan RiwayatTransaksi. Objek RiwayatTransaksi dibuat langsung di dalam konstruktor TokoSkincare dan hanya dimiliki oleh toko tersebut. Riwayat transaksi tidak memiliki fungsi tanpa toko, sehingga jika toko dihapus maka riwayatnya ikut hilang.

Inheritance

Superclass pada program ini adalah ProdukSkincare, sedangkan subclass-nya adalah ProdukSunscreen dan ProdukSerum. Kedua subclass memanggil konstruktor superclass menggunakan super().init() untuk mengisi atribut bawaan produk.

Setiap subclass memiliki atribut tambahan yang membedakannya. ProdukSunscreen memiliki atribut spf, sedangkan ProdukSerum memiliki atribut kandungan_aktif.

Method overriding diterapkan pada beberapa method. Pada ProdukSunscreen, method hitung_harga_jual() didefinisikan ulang sehingga produk dengan SPF 50 ke atas mendapat potongan harga 10 persen. Pada ProdukSerum, method kurangi_stok() didefinisikan ulang untuk membatasi pembelian maksimal 5 buah per transaksi, kemudian tetap memanggil method milik superclass dengan super(). Method tampilkan_info() juga di-override pada kedua subclass untuk menampilkan atribut tambahan masing-masing.

Untuk tingkat akses, atribut _harga dan _stok pada superclass dibuat protected karena perlu diakses langsung oleh subclass, misalnya ketika menghitung harga promo atau mengurangi stok. Atribut __harga_modal dibuat private karena merupakan data rahasia yang hanya boleh dipakai oleh superclass. Data tersebut hanya bisa dilihat hasilnya melalui method hitung_margin().

Konsep OOP Lainnya

Program ini juga menggunakan encapsulation dengan property dan setter yang memvalidasi nilai harga, stok, dan jumlah beli. Class method dipakai pada dari_dict(), buat_transaksi_otomatis(), dan atur_pajak(). Static method dipakai pada validasi_jenis_produk(), validasi_format_tanggal(), dan format_rupiah(). Polymorphism terlihat ketika toko memanggil tampilkan_info() untuk semua produk, dan setiap jenis produk menampilkan hasil yang berbeda.

Cara Menjalankan

Program membutuhkan Python 3.8 atau yang lebih baru dan tidak memerlukan library tambahan. Jalankan dengan perintah berikut:
python posttest_skincare.py