secret_number = 123
guess_number = int(input("Masukkan Tebak Angka: "))

while guess_number != secret_number:
    print("Tebakan Salah, Silakan Coba Lagi")
    guess_number = int(input("Masukkan Tebak Angka: "))

print("Selamat...! Tebakan Anda Benar!!")