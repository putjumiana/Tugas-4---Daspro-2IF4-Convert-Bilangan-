def bin_to_decimal(binary):
    return int(binary, 2)

def decimal_to_bin_8bit(decimal):
    binary = bin(decimal)[2:] 
    return binary.zfill(8) if len(binary) < 8 else binary[-8:] 

def oct_to_decimal(octal):
    return int(octal, 8)

def decimal_to_oct(decimal):
    return oct(decimal)[2:]

def hex_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def decimal_to_hex(decimal):
    return hex(decimal)[2:]

def main():
    while True:
        print("\nPilih opsi:")
        print("1. Konversi Biner ke Desimal")
        print("2. Konversi Desimal ke Biner (8 bit)")
        print("3. Konversi Oktal ke Desimal")
        print("4. Konversi Desimal ke Oktal")
        print("5. Konversi Heksadesimal ke Desimal")
        print("6. Konversi Desimal ke Heksadesimal")
        print("7. Keluar")
        
        choice = input("Masukkan pilihan Anda: ")
        if choice == '1': # Tambahkan kode konversi biner ke desimal
            binary = input("Masukkan bilangan biner: ")
            print("Hasil konversi:", bin_to_decimal(binary))
        elif choice == '2':
            decimal = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", decimal_to_bin_8bit(decimal))
        elif choice == '3': # Tambahkan kode konversi oktal ke desimal
            octal = input("Masukkan bilangan oktal: ")
            print("Hasil konversi:", oct_to_decimal(octal))
        elif choice == '4': # Tambahkan kode konversi desimal ke oktal
            decimal = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", decimal_to_oct(decimal))
        elif choice == '5': # Tambahkan kode konversi heksadesimal ke desimal
            hexadecimal = input("Masukkan bilangan heksadesimal: ")
            print("Hasil konversi:", hex_to_decimal(hexadecimal))
        elif choice == '6': # Tambahkan kode konversi desimal ke heksadesimal
            decimal = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", decimal_to_hex(decimal))
        elif choice == '7':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
