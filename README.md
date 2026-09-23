# Sistem Manajemen Penjualan Toko Skincare "Skin Studio"

Program ini dibuat untuk tugas praktikum PBO, dengan tema toko skincare bernama Skin Studio. Konsep OOP yang dipakai mengikuti tiga modul yang sudah dipelajari: Class & Object, Atribut & Method, serta Encapsulation & Property.

## Class yang dipakai

Ada tiga class utama: `ProdukSkincare`, `Transaksi`, dan `TokoSkincare`. Ketiganya tidak pakai inheritance, tapi saling berinteraksi lewat objek satu sama lain — misalnya `Transaksi` dibuat dari objek `ProdukSkincare`, dan `TokoSkincare` menyimpan kumpulan objek `ProdukSkincare` serta `Transaksi`.

**ProdukSkincare** mengurus data satu produk (id, nama, jenis, harga, stok). Harga dan stok disimpan sebagai atribut private, jadi hanya bisa diubah lewat property yang sudah ada validasinya. Ada method untuk kurangi stok dan tambah stok, ditambah classmethod untuk bikin produk dari dictionary dan staticmethod untuk cek jenis produk valid atau tidak.

**Transaksi** mencatat satu transaksi pembelian: id transaksi, tanggal, produk yang dibeli, jumlah, dan total harga. Jumlah beli juga disimpan private dan divalidasi lewat setter. Ada method untuk hitung total harga dan cetak struk.

**TokoSkincare** menyimpan daftar produk dan riwayat transaksi suatu cabang toko. Dari sini bisa tambah produk, tampilkan semua produk, update stok, hapus produk, dan lihat riwayat transaksi.

## Kenapa harga/stok/jumlah dibikin private

Karena data seperti itu tidak boleh diubah sembarangan dari luar tanpa validasi. Makanya dipakai `@property` sebagai getter dan `@nama.setter` sebagai setter — setiap kali nilainya mau diganti, setter otomatis mengecek dulu apakah valid. Kalau tidak valid (misalnya harga negatif), program akan `raise ValueError` dan perubahan ditolak.

## Cara jalanin

```
python main.py
```

Tidak perlu install apa-apa, cukup Python biasa.

## Yang didemonstrasikan di bagian testing

Di bagian bawah `main.py`, program ini:
- Bikin minimal 2 objek untuk tiap class
- Manggil semua jenis method yang ada (instance, class, static)
- Nyoba setter dengan input valid dan tidak valid, buat buktiin validasinya jalan (misal masukin harga -1000, programnya bakal nolak dan kasih pesan error, bukan malah nerima nilai itu)

Tinggal jalanin filenya dan lihat outputnya di terminal, semua langkah pengujian sudah tercetak urut.
