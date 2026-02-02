import json

saldo = 0
pemasukan = []
pengeluaran = []

def load_data():
    global saldo, pemasukan, pengeluaran
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            saldo = data.get('saldo', 0)
            pemasukan = data.get('pemasukan', [])
            pengeluaran = data.get('pengeluaran', [])
    except FileNotFoundError:
        pass

def save_data():
    data = {
        'saldo': saldo,
        'pemasukan': pemasukan,
        'pengeluaran': pengeluaran
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)

def tambah_pemasukan():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        saldo += jumlah
        pemasukan.append(jumlah)
        print("Pemasukan berhasil ditambahkan!")
        save_data()
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
        if saldo >= jumlah:
            saldo -= jumlah
            pengeluaran.append(jumlah)
            print("Pengeluaran berhasil ditambahkan!")
            save_data()
        else:
            print("Saldo tidak cukup!")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

def lihat_saldo():
    print(f"Saldo saat ini: Rp {saldo:.2f}")

def laporan():
    total_pemasukan = sum(pemasukan)
    total_pengeluaran = sum(pengeluaran)
    print("=== Laporan Rekap ===")
    print(f"Total Pemasukan: Rp {total_pemasukan:.2f}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran:.2f}")
    print(f"Saldo Saat Ini: Rp {saldo:.2f}")
    print("Detail Pemasukan:")
    for i, p in enumerate(pemasukan, 1):
        print(f"{i}. Rp {p:.2f}")
    print("Detail Pengeluaran:")
    for i, p in enumerate(pengeluaran, 1):
        print(f"{i}. Rp {p:.2f}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Laporan")
    print("5. Keluar")

load_data()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        laporan()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
