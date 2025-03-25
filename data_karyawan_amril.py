# Data Karyawan 
karyawan = [
    ("K001", "Andi", "Manager"),
    ("K002", "Budi", "Kasir"),
    ("K003", "Citra", "Staff"),
    ("K004", "Indah", "Pramuniaga/Sales Associate"),
    ("K005", "Linda", "Stocker/merchandiser"),
    ("K006", "Bayu", "Scurity/Satpam"),
    ("K007", "Fendi", "Cleaning Service"),
    ("K008", "Alvian", "Admin/Back Office"),
    ("K009", "Riski", "Customer Service")
]

# Data Produk: ID Produk -> (Nama Produk, Harga Satuan)
produk = {
    "P001": ("Pulpen", 3000),
    "P002": ("Pensil", 2000),
    "P003": ("Spidol", 8000),
    "P004": ("Buku Catatan", 15000),
    "P005": ("Kertas Prin", 60000),
    "P006": ("Penghapus", 2000),
    "P007": ("Stabilo", 60000),
    "P008": ("Maf", 1000),
    "P009": ("Gunting", 6000),
    "P010": ("Slotip", 10000),
    "P011": ("Staples", 4000),
    "P012": ("Sanitizer Tangan", 9000),
    "P013": ("Tisu", 2000),
    "P014": ("Komputer/Labtop", 10000000),
    "P015": ("Printer", 1000000),
    "P016": ("Waifi", 500000),
    "P017": ("Cctv", 1000000),
    "P018": ("Penggaris", 2000),
    "P019": ("Makanan 1 paket", 20000),
    "P020": ("Proyektor", 2000000)
}

# Data Transaksi: (ID Transaksi, ID Produk, Jumlah)
transaksi = [
    ("TR001", "P001", 2),
    ("TR002", "P002", 5),
    ("TR003", "P003", 1)
]

# ======= FUNGSI KARYAWAN =======
def tambah_karyawan():
    id_karyawan = input("Masukkan ID Karyawan: ")
    nama = input("Masukkan Nama: ")
    jabatan = input("Masukkan Jabatan: ")
    karyawan.append((id_karyawan, nama, jabatan))
    print("Data karyawan berhasil ditambahkan.")

def tampilkan_karyawan():
    print("\nData Karyawan:")
    for data in karyawan:
        print(f"ID: {data[0]}, Nama: {data[1]}, Jabatan: {data[2]}")

# ======= FUNGSI PRODUK =======
def tambah_produk():
    id_produk = input("Masukkan ID Produk: ").upper()
    if id_produk in produk:
        print("ID Produk sudah ada!")
        return
    nama = input("Masukkan Nama Produk: ")
    try:
        harga = int(input("Masukkan Harga Produk: "))
    except ValueError:
        print("Harga harus berupa angka.")
        return

    produk[id_produk] = (nama, harga)
    print("Produk berhasil ditambahkan.")

def tampilkan_produk():
    print("\nDaftar Produk:")
    for kode, (nama, harga) in produk.items():
        print(f"ID: {kode}, Nama: {nama}, Harga: Rp{harga}")

# ======= FUNGSI TRANSAKSI =======
def tambah_transaksi():
    id_transaksi = input("Masukkan ID Transaksi: ")
    id_produk = input("Masukkan ID Produk: ").upper()

    if id_produk not in produk:
        print("ID Produk tidak ditemukan!")
        return

    try:
        jumlah = int(input("Masukkan Jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    transaksi.append((id_transaksi, id_produk, jumlah))
    print("Transaksi berhasil ditambahkan.")

def tampilkan_transaksi():
    print("\nData Transaksi:")
    for t in transaksi:
        id_trx, id_produk, jumlah = t
        nama_produk, harga = produk.get(id_produk, ("Tidak diketahui", 0))
        total = jumlah * harga
        print(f"ID Transaksi: {id_trx}, Produk: {nama_produk}, Jumlah: {jumlah}, Harga Satuan: Rp{harga}, Total: Rp{total}")

# ======= MENU UTAMA =======
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Manajemen Karyawan")
    print("2. Manajemen Produk")
    print("3. Manajemen Transaksi")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        while True:
            print("\n-- Menu Karyawan --")
            print("1. Tambah Karyawan")
            print("2. Lihat Data Karyawan")
            print("3. Kembali ke Menu Utama")
            sub = input("Pilih menu (1-3): ")
            if sub == "1":
                tambah_karyawan()
            elif sub == "2":
                tampilkan_karyawan()
            elif sub == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "2":
        while True:
            print("\n-- Menu Produk --")
            print("1. Tambah Produk")
            print("2. Lihat Daftar Produk")
            print("3. Kembali ke Menu Utama")
            sub = input("Pilih menu (1-3): ")
            if sub == "1":
                tambah_produk()
            elif sub == "2":
                tampilkan_produk()
            elif sub == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "3":
        while True:
            print("\n-- Menu Transaksi --")
            print("1. Tambah Transaksi")
            print("2. Lihat Data Transaksi")
            print("3. Kembali ke Menu Utama")
            sub = input("Pilih menu (1-3): ")
            if sub == "1":
                tambah_transaksi()
            elif sub == "2":
                tampilkan_transaksi()
            elif sub == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
