soc      = float(input('SOC (%): '))
tegangan = float(input('Tegangan (V): '))
suhu     = float(input('Suhu (C): '))
daya     = float(input('Daya (W): '))
sensor_aktif = input('Sensor aktif? (y/n): ').lower() == 'y'
 
if soc < 20:
    status_soc = 'Rendah'
elif soc <= 80:
    status_soc = 'Normal'
else:
    status_soc = 'Tinggi'
 
if tegangan < 11.5:
    status_tegangan = 'Rendah'
elif tegangan <= 14.4:
    status_tegangan = 'Normal'
else:
    status_tegangan = 'Tinggi'
 
suhu_aman = suhu <= 40
arah_daya = 'Mengisi (charging)' if daya < 0 else 'Mengosongkan (discharging)'
data_valid = (0 <= soc <= 100) and not (tegangan < 0)
 
aman_beroperasi = (
    data_valid and status_soc == 'Normal'
    and status_tegangan == 'Normal' and suhu_aman and sensor_aktif
)
 
if not data_valid:
    print('STATUS AKHIR: DATA TIDAK VALID - abaikan pembacaan ini')
elif aman_beroperasi:
    print('STATUS AKHIR: AMAN - operasi normal')
else:
    alasan = []
    if status_soc != 'Normal': alasan.append('SOC ' + status_soc.lower())
    if status_tegangan != 'Normal': alasan.append('tegangan ' + status_tegangan.lower())
    if not suhu_aman: alasan.append('suhu di atas 40C')
    if not sensor_aktif: alasan.append('sensor nonaktif')
    print('STATUS AKHIR: PERLU PERHATIAN -', ', '.join(alasan))
