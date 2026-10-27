class ProdukSkincare:
    nama_toko = "Skin Studio"
    total_produk_terdaftar = 0
    jenis_valid = ["cleanser", "toner", "serum", "moisturizer", "sunscreen", "masker"]

    def __init__(self, id_produk, nama_produk, jenis_produk, harga, stok, harga_modal=0):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

        self._harga = 0
        self._stok = 0
        self.harga = harga
        self.stok = stok

        self.__harga_modal = harga_modal

        ProdukSkincare.total_produk_terdaftar += 1

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, value):
        if value < 0:
            raise ValueError("Harga tidak boleh negatif.")
        self._harga = value

    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, value):
        if value < 0:
            raise ValueError("Stok tidak boleh negatif.")
        self._stok = value

    def hitung_margin(self):
        return self._harga - self.__harga_modal

    def hitung_harga_jual(self):
        return self._harga

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah pengurangan harus lebih dari 0.")
            return False
        if jumlah > self._stok:
            print(f"Stok {self.nama_produk} tidak mencukupi (sisa {self._stok}).")
            return False
        self._stok -= jumlah
        return True

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah restock harus lebih dari 0.")
            return False
        self._stok += jumlah
        print(f"Stok {self.nama_produk} bertambah {jumlah}, sekarang {self._stok}.")
        return True

    def tampilkan_info(self):
        print(f"[{self.id_produk}] {self.nama_produk} ({self.jenis_produk}) - "
              f"Rp{self._harga} | Stok: {self._stok}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["id_produk"], data["nama_produk"], data["jenis_produk"],
                   data["harga"], data["stok"])

    @classmethod
    def info_kelas(cls):
        print(f"Toko: {cls.nama_toko} | Total produk terdaftar: {cls.total_produk_terdaftar}")

    @staticmethod
    def validasi_jenis_produk(jenis):
        return jenis.lower() in ProdukSkincare.jenis_valid

class ProdukSunscreen(ProdukSkincare):
    def __init__(self, id_produk, nama_produk, harga, stok, spf, harga_modal=0):
        super().__init__(id_produk, nama_produk, "sunscreen", harga, stok, harga_modal)
        self.spf = spf 

    def hitung_harga_jual(self):
        if self.spf >= 50:
            return self._harga * 0.9
        return self._harga

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"    SPF: {self.spf} | Harga jual (promo): Rp{int(self.hitung_harga_jual())}")

class ProdukSerum(ProdukSkincare):
    def __init__(self, id_produk, nama_produk, harga, stok, kandungan_aktif, harga_modal=0):
        super().__init__(id_produk, nama_produk, "serum", harga, stok, harga_modal)
        self.kandungan_aktif = kandungan_aktif  

    def kurangi_stok(self, jumlah):
        if jumlah > 5:
            print(f"Serum {self.nama_produk} maksimal 5 per transaksi.")
            return False
        return super().kurangi_stok(jumlah)

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"    Kandungan aktif: {self.kandungan_aktif}")

class Pelanggan:
    def __init__(self, id_pelanggan, nama):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.poin = 0

    def tambah_poin(self, poin):
        self.poin += poin

class Transaksi:
    mata_uang = "Rp"
    total_transaksi_dibuat = 0
    pajak_persen = 0

    def __init__(self, id_transaksi, tanggal, produk, jumlah, pelanggan=None):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.produk = produk        
        self.pelanggan = pelanggan    
        self.id_produk = produk.id_produk
        self.nama_produk = produk.nama_produk
        self.__harga_satuan = produk.hitung_harga_jual() 
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
        if self.pelanggan:
            print(f"Pelanggan : {self.pelanggan.nama}")
        print(f"Produk    : {self.nama_produk} ({self.id_produk})")
        print(f"Jumlah    : {self.__jumlah}")
        print(f"Harga/pcs : {Transaksi.mata_uang}{int(self.__harga_satuan)}")
        print(f"Total     : {Transaksi.mata_uang}{int(self.__total_harga)}")
        print("=" * 35)

    @classmethod
    def buat_transaksi_otomatis(cls, produk, jumlah, tanggal, pelanggan=None):
        id_transaksi = f"TRX{cls.total_transaksi_dibuat + 1:04d}"
        return cls(id_transaksi, tanggal, produk, jumlah, pelanggan)

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

class RiwayatTransaksi:
    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.__daftar = []

    @property
    def daftar(self):
        return self.__daftar

    def catat(self, transaksi):
        self.__daftar.append(transaksi)

    def tampilkan(self):
        print(f"\nRiwayat Transaksi - Cabang {self.nama_cabang}")
        print("-" * 35)
        if not self.__daftar:
            print("Belum ada transaksi.")
            return
        for trx in self.__daftar:
            trx.cetak_struk()

class TokoSkincare:
    nama_perusahaan = "PT Glow Beauty Indonesia"
    alamat_pusat = "Jl. Kecantikan No. 1, Jakarta"
    jam_operasional = "09:00 - 21:00"

    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self.__daftar_produk = {}                      
        self.__riwayat = RiwayatTransaksi(nama_cabang)  

    @property
    def daftar_produk(self):
        return self.__daftar_produk

    @property
    def riwayat_transaksi(self):
        return self.__riwayat.daftar

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
            self.__riwayat.catat(transaksi)
            if transaksi.pelanggan:
                transaksi.pelanggan.tambah_poin(transaksi.jumlah * 10)
            print(f"Transaksi {transaksi.id_transaksi} berhasil dicatat.")
        return berhasil

    def tampilkan_riwayat_transaksi(self):
        self.__riwayat.tampilkan()

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

    print("=== Bikin produk ===")
    produk1 = ProdukSkincare("P001", "Facial Wash Aloe Vera", "cleanser", 35000, 50, harga_modal=20000)
    produk2 = ProdukSerum("P002", "Vitamin C Serum", 89000, 30, "Vitamin C 10%", harga_modal=55000)
    produk3 = ProdukSunscreen("P003", "Sunscreen SPF50", 65000, 40, 50, harga_modal=40000)

    for p in (produk1, produk2, produk3):
        p.tampilkan_info()
    ProdukSkincare.info_kelas()
    print("Margin sunscreen:", produk3.hitung_margin())

    print("\n=== Coba ubah harga ===")
    produk1.harga = 40000
    print("Harga facial wash sekarang:", produk1.harga)
    try:
        produk1.harga = -1000
    except ValueError as e:
        print("Gagal:", e)

    print("\n=== Coba stok serum ===")
    produk2.tambah_stok(10)
    produk2.kurangi_stok(8)  
    produk2.kurangi_stok(3)   

    print("\n=== Masukin produk ke toko ===")
    toko1 = TokoSkincare("Cabang Balikpapan")
    toko2 = TokoSkincare.buat_cabang_default()
    for p in (produk1, produk2, produk3):
        toko1.tambah_produk(p)
    toko1.tampilkan_semua_produk()
    toko2.tambah_produk(produk1)  
    toko2.tampilkan_semua_produk()

    print("\n=== Transaksi ===")
    Transaksi.atur_pajak(11)
    budi = Pelanggan("C001", "Budi")
    trx1 = Transaksi("TRX0001", "2026-09-22", produk1, 3, budi)
    trx2 = Transaksi.buat_transaksi_otomatis(produk3, 2, "2026-09-22", budi)
    trx1.cetak_struk()
    trx2.cetak_struk()

    print("\n=== Catat transaksi ke toko ===")
    toko1.proses_transaksi(trx1)
    toko1.proses_transaksi(trx2)
    toko1.tampilkan_riwayat_transaksi()
    print(f"Poin {budi.nama}: {budi.poin}")

    print("\n=== Hapus produk dari toko ===")
    toko1.hapus_produk("P003")
    print("Produknya masih ada:", produk3.nama_produk)
    toko1.tampilkan_semua_produk()
    print(TokoSkincare.format_rupiah(1250000))