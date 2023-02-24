from app import pola_bintang, sub_bintang

print("")
print("## Program Bangun Ruang Berbentuk Bintang ##")
print("============================================")
print("Silahkan pilih menu dibawah ini: ")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga Siku Siku")
print("4. Segitiga Terbalik")
print("5. Piramida")
print("6. Piramida Terbalik")
print("7. Belah Ketupat")
pilihan = int(input("Masukan pilihan kamu (1-7): "))

if pilihan == 1:
    print("")
    print("## Persegi ##")
    print("==================")

    num_1 = int(input("Input besar persegi: "))
    result = pola_bintang(num_1)
    result.persegi_bintang()

elif pilihan == 2:
    print("")
    print("## Persegi Panjang ##")
    print("=====================")

    num_1 = int(input("Input tinggi persegi panjang: "))
    num_2 = int(input("Input lebar persegi panjang: "))
    result = sub_bintang(num_1,num_2)
    result.persegi_panjang()

elif pilihan == 3:
    print("")
    print("## Segitiga Siku-Siku ##")
    print("========================")

    num_1 = int(input("Input besar segitiga: "))
    result = pola_bintang(num_1)
    result.segitiga_bintang()

elif pilihan == 4:
    print("")
    print("## Segitiga Terbalik ##")
    print("=======================")

    num_1 = int(input("Input besar segitiga: "))
    result = pola_bintang(num_1)
    result.segitiga_tebalik()

elif pilihan == 5:
    print("")
    print("## Piramida ##")
    print("==============")

    num_1 = int(input("Input besar piramida: "))
    result = pola_bintang(num_1)
    result.piramida()

elif pilihan == 6:
    print("")
    print("## Piramida Tebalik ##")
    print("======================")

    num_1 = int(input("Input besar piramida: "))
    result = pola_bintang(num_1)
    result.piramida_tebalik()

elif pilihan == 7:
    print("")
    print("## Belah Ketupat ##")
    print("===================")

    num_1 = int(input("Input besar belah ketupat: "))
    result = pola_bintang(num_1)
    result.belah_ketupat()