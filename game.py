secret_number = 777
guess_number = int(input("Masukkan Tebak Angka:"))

while guess_number != secret_number:
    print("Tebakan Salah, Silakan Coba Lagi")
    print("anda terjebak dalam perputaran abadi")
    guess_number = int(input("Masukkan Tebak Angka:"))

print("Selamat... ! Tebakan Anda Benar!!")
print("kod e ini saa buat di codespace")