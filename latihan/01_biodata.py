TAHUN_SEKARANG = 2026

nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

perkiraan_umur = TAHUN_SEKARANG - tahun_lahir

print()
print(f"Nama  : {nama}")
print(f"NIM   : {nim}")
print(f"Kelas : {kelas}")
print(f"Umur  : sekitar {perkiraan_umur} tahun")