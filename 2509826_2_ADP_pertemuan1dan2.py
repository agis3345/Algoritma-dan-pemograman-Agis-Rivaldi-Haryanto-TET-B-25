print("Selamat datang di mata kuliah Algoritma, Data, dan Pemrograman")
print("Program Studi Teknik Energi Terbarukan")
daya_watt = 200
durasi_jam = 5
energi_wh = daya_watt * durasi_jam
energi_kwh = energi_wh / 1000
print("Energi ideal (Wh):", energi_wh)
print("Energi ideal (kWh):", energi_kwh)

daya_watt = 300
durasi_jam = 7
energi_wh = daya_watt * durasi_jam
energi_kwh = energi_wh / 1000
print("Energi ideal (Wh):", energi_wh)
print("Energi ideal (kWh):", energi_kwh)

daya_watt = 450
durasi_jam = 9
energi_wh = daya_watt * durasi_jam
energi_kwh = energi_wh / 1000
print("Energi ideal (Wh):", energi_wh)
print("Energi ideal (kWh):", energi_kwh)

daya_panel = 200
durasi = 5
energi_wh = daya_panel * durasi
energi_kwh = energi_wh / 1000
print("=== PERHITUNGAN ENERGI PANEL SURYA ===")
print("Daya Panel:", daya_panel, "W")
print("Durasi:", durasi, "Jam")
print("Energi yang dihasilkan:", energi_wh, "Wh")
print("Energi yang dihasilkan:", energi_kwh, "kWh")

nama_sistem = "PLTS Atap"
daya_watt = 500
durasi_jam = 4.0
efisiensi = 0.90

print(type(nama_sistem))
print(type(daya_watt))
print(type(durasi_jam))
print(type(efisiensi))

daya_watt = float(input("Masukkan daya panel (W): "))
durasi_jam = float(input("Masukkan durasi efektif (jam): "))
efisiensi = float(input("Masukkan efisiensi sistem (0-1): "))

energi_wh = daya_watt * durasi_jam * efisiensi
energi_kwh = energi_wh / 1000

print(f"Energi keluaran: {energi_wh:.2f} Wh")
print(f"Energi keluaran: {energi_kwh:.3f} kWh")

nama_sistem = input("Nama sistem: ")

daya_watt = float(input("Masukkan daya panel (W): "))
durasi_jam = float(input("Masukkan durasi efektif (jam): "))
efisiensi = float(input("Masukkan efisiensi sistem (0-1): "))

energi_wh = daya_watt * durasi_jam * efisiensi
energi_kwh = energi_wh / 1000

print(f"{nama_sistem} menghasilkan estimasi {energi_kwh:.3f} kWh.")

nama_sistem = input("Nama sistem: ")

daya_watt = float(input("Masukkan daya panel (W): "))
durasi_jam = float(input("Masukkan durasi efektif (jam): "))
efisiensi = float(input("Masukkan efisiensi sistem (0-1): "))

energi_wh = daya_watt * durasi_jam * efisiensi
energi_kwh = energi_wh / 1000

print(f"{nama_sistem} menghasilkan estimasi {energi_kwh:.3f} kWh.")

nama_sistem = input("Nama sistem: ")

daya_watt = float(input("Masukkan daya panel (W): "))
durasi_jam = float(input("Masukkan durasi efektif (jam): "))
efisiensi = float(input("Masukkan efisiensi sistem (0-1): "))

energi_wh = daya_watt * durasi_jam * efisiensi
energi_kwh = energi_wh / 1000

print(f"{nama_sistem} menghasilkan estimasi {energi_kwh:.3f} kWh.")
