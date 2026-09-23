class ProdukSkincare:
    nama_toko = "Skin Studio"
    total_produk_terdaftar = 0
    jenis_valid = ["cleanser", "toner", "serum", "moisturizer", "sunscreen", "masker"]

    def __init__(self, id_produk, nama_produk, jenis_produk, harga, stok):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

        self.__harga = 0
        self.__stok = 0
        self.harga = harga
        self.stok = stok

        ProdukSkincare.total_produk_terdaftar += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        if value < 0:
            raise ValueError("Harga tidak boleh negatif.")
        self.__harga = value

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        if value < 0:
            raise ValueError("Stok tidak boleh negatif.")
        self.__stok = value

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah pengurangan harus lebih dari 0.")
            return False
        if jumlah > self.__stok:
            print(f"Stok {self.nama_produk} tidak mencukupi (sisa {self.__stok}).")
            return False
        self.__stok -= jumlah
        return True

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah restock harus lebih dari 0.")
            return False
        self.__stok += jumlah
        print(f"Stok {self.nama_produk} bertambah {jumlah}, sekarang {self.__stok}.")
        return True

    def tampilkan_info(self):
        print(f"[{self.id_produk}] {self.nama_produk} ({self.jenis_produk}) - "
              f"Rp{self.__harga} | Stok: {self.__stok}")

    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["id_produk"],
            data["nama_produk"],
            data["jenis_produk"],
            data["harga"],
            data["stok"],
        )

    @classmethod
    def info_kelas(cls):
        print(f"Toko: {cls.nama_toko} | Total produk terdaftar: {cls.total_produk_terdaftar}")

    @staticmethod
    def validasi_jenis_produk(jenis):
        return jenis.lower() in ProdukSkincare.jenis_valid


class Transaksi:
    mata_uang = "Rp"
    total_transaksi_dibuat = 0
    pajak_persen = 0

    def __init__(self, id_transaksi, tanggal, produk, jumlah):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.id_produk = produk.id_produk
        self.nama_produk = produk.nama_produk

        self.__harga_satuan = produk.harga
        self.__jumlah = 0
        self.jumlah = jumlah
        self.__total_harga = 0

        Transaksi.total_transaksi_dibuat += 1

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, value):
        if value <= 0:
            raise ValueError("Jumlah beli harus lebih dari 0.")
        self.__jumlah = value

    @property
    def total_harga(self):
        return self.__total_harga

    def hitung_total_harga(self):
        subtotal = self.__harga_satuan * self.__jumlah
        pajak = subtotal * (Transaksi.pajak_persen / 100)
        self.__total_harga = subtotal + pajak
        return self.__total_harga

    def cetak_struk(self):
        self.hitung_total_harga()
        print("=" * 35)
        print(f"STRUK TRANSAKSI - {self.id_transaksi}")
        print(f"Tanggal   : {self.tanggal}")
        print(f"Produk    : {self.nama_produk} ({self.id_produk})")
        print(f"Jumlah    : {self.__jumlah}")
        print(f"Harga/pcs : {Transaksi.mata_uang}{self.__harga_satuan}")
        print(f"Total     : {Transaksi.mata_uang}{self.__total_harga}")
        print("=" * 35)

    @classmethod
    def buat_transaksi_otomatis(cls, produk, jumlah, tanggal):
        id_transaksi = f"TRX{cls.total_transaksi_dibuat + 1:04d}"
        return cls(id_transaksi, tanggal, produk, jumlah)

    @classmethod
    def atur_pajak(cls, persen):
        if persen < 0:
            print("Pajak tidak boleh negatif.")
            return
        cls.pajak_persen = persen
        print(f"Pajak transaksi diatur menjadi {persen}%.")

    @staticmethod
    def validasi_format_tanggal(tanggal):
        bagian = tanggal.split("-")
        if len(bagian) != 3:
            return False
        tahun, bulan, hari = bagian
        return len(tahun) == 4 and len(bulan) == 2 and len(hari) == 2


class TokoSkincare:
    nama_perusahaan = "PT Glow Beauty Indonesia"
    alamat_pusat = "Jl. Kecantikan No. 1, Jakarta"
    jam_operasional = "09:00 - 21:00"

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.__daftar_produk = {}
        self.__riwayat_transaksi = []

    @property
    def daftar_produk(self):
        return self.__daftar_produk

    @property
    def riwayat_transaksi(self):
        return self.__riwayat_transaksi

    def tambah_produk(self, produk):
        if produk.id_produk in self.__daftar_produk:
            print(f"Produk dengan id {produk.id_produk} sudah ada.")
            return False
        self.__daftar_produk[produk.id_produk] = produk
        print(f"Produk {produk.nama_produk} berhasil ditambahkan ke cabang {self.nama_cabang}.")
        return True

    def tampilkan_semua_produk(self):
        print(f"\nDaftar Produk - Cabang {self.nama_cabang}")
        print("-" * 35)
        if not self.__daftar_produk:
            print("Belum ada produk.")
            return
        for produk in self.__daftar_produk.values():
            produk.tampilkan_info()

    def update_stok(self, id_produk, jumlah, mode="tambah"):
        produk = self.__daftar_produk.get(id_produk)
        if produk is None:
            print(f"Produk id {id_produk} tidak ditemukan.")
            return False
        if mode == "tambah":
            return produk.tambah_stok(jumlah)
        elif mode == "kurang":
            return produk.kurangi_stok(jumlah)
        else:
            print("Mode harus 'tambah' atau 'kurang'.")
            return False

    def hapus_produk(self, id_produk):
        if id_produk in self.__daftar_produk:
            nama = self.__daftar_produk[id_produk].nama_produk
            del self.__daftar_produk[id_produk]
            print(f"Produk {nama} berhasil dihapus.")
            return True
        print(f"Produk id {id_produk} tidak ditemukan.")
        return False

    def proses_transaksi(self, transaksi):
        berhasil = self.update_stok(transaksi.id_produk, transaksi.jumlah, mode="kurang")
        if berhasil:
            self.__riwayat_transaksi.append(transaksi)
            print(f"Transaksi {transaksi.id_transaksi} berhasil dicatat.")
        return berhasil

    def tampilkan_riwayat_transaksi(self):
        print(f"\nRiwayat Transaksi - Cabang {self.nama_cabang}")
        print("-" * 35)
        if not self.__riwayat_transaksi:
            print("Belum ada transaksi.")
            return
        for trx in self.__riwayat_transaksi:
            trx.cetak_struk()

    @classmethod
    def buat_cabang_default(cls):
        return cls(f"{cls.nama_perusahaan} - Cabang Utama")

    @staticmethod
    def format_rupiah(angka):
        teks = str(int(angka))
        hasil = ""
        hitung = 0
        for digit in reversed(teks):
            hasil = digit + hasil
            hitung += 1
            if hitung % 3 == 0 and hitung != len(teks):
                hasil = "." + hasil
        return "Rp" + hasil


if __name__ == "__main__":

    print("--- 1. Membuat Objek Produk Skincare ---")
    produk1 = ProdukSkincare("P001", "Facial Wash Aloe Vera", "cleanser", 35000, 50)
    produk2 = ProdukSkincare("P002", "Vitamin C Serum", "serum", 89000, 30)

    produk3 = ProdukSkincare.dari_dict({
        "id_produk": "P003",
        "nama_produk": "Sunscreen SPF50",
        "jenis_produk": "sunscreen",
        "harga": 65000,
        "stok": 40,
    })

    produk1.tampilkan_info()
    produk2.tampilkan_info()
    produk3.tampilkan_info()
    ProdukSkincare.info_kelas()

    print("\n--- 2. Static Method: Validasi Jenis Produk ---")
    print("cleanser valid?", ProdukSkincare.validasi_jenis_produk("cleanser"))
    print("hair-oil valid?", ProdukSkincare.validasi_jenis_produk("hair-oil"))

    print("\n--- 3. Uji Setter Harga & Stok (Valid & Tidak Valid) ---")
    produk1.harga = 40000
    print("Harga diubah menjadi:", produk1.harga)

    try:
        produk1.harga = -1000
    except ValueError as e:
        print("Validasi:", e)

    produk1.stok = 45
    print("Stok diubah menjadi:", produk1.stok)

    try:
        produk1.stok = -5
    except ValueError as e:
        print("Validasi:", e)

    produk1.tampilkan_info()

    print("\n--- 4. Instance Method: Tambah/Kurangi Stok ---")
    produk2.tambah_stok(10)
    produk2.kurangi_stok(200)
    produk2.kurangi_stok(5)

    print("\n--- 5. Membuat Objek Toko Skincare ---")
    toko1 = TokoSkincare("Cabang Balikpapan")
    toko2 = TokoSkincare.buat_cabang_default()

    toko1.tambah_produk(produk1)
    toko1.tambah_produk(produk2)
    toko1.tambah_produk(produk3)
    toko1.tampilkan_semua_produk()

    toko2.tambah_produk(
        ProdukSkincare("P010", "Moisturizer Gel", "moisturizer", 55000, 20)
    )
    toko2.tampilkan_semua_produk()

    print("\n--- 6. Static Method: Format Rupiah ---")
    print(TokoSkincare.format_rupiah(1250000))

    print("\n--- 7. Membuat & Memproses Transaksi ---")
    Transaksi.atur_pajak(11)

    trx1 = Transaksi("TRX0001", "2026-09-22", produk1, 3)
    trx1.hitung_total_harga()
    trx1.cetak_struk()

    trx2 = Transaksi.buat_transaksi_otomatis(produk3, 2, "2026-09-22")
    trx2.cetak_struk()

    print("\n--- 8. Uji Setter Jumlah Transaksi (Valid & Tidak Valid) ---")
    trx3 = Transaksi("TRX0003", "2026-09-22", produk2, 2)
    trx3.jumlah = 5
    print("Jumlah diubah menjadi:", trx3.jumlah)

    try:
        trx3.jumlah = -2
    except ValueError as e:
        print("Validasi:", e)

    trx3.cetak_struk()

    print("\n--- 9. Static Method: Validasi Format Tanggal ---")
    print("2026-09-22 valid?", Transaksi.validasi_format_tanggal("2026-09-22"))
    print("22-09-2026 valid?", Transaksi.validasi_format_tanggal("22-09-2026"))

    print("\n--- 10. Mencatat Transaksi ke Toko & Lihat Riwayat ---")
    toko1.proses_transaksi(trx1)
    toko1.proses_transaksi(trx3)
    toko1.tampilkan_riwayat_transaksi()

    print("\n--- 11. Update Stok & Hapus Produk dari Toko ---")
    toko1.update_stok("P002", 10, mode="tambah")
    toko1.hapus_produk("P010")
    toko1.hapus_produk("P003")
    toko1.tampilkan_semua_produk()