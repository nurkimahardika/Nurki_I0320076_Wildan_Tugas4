
dua_angka = input('Tulis 2 angka yang dipisah oleh spasi antara keduanya!=')
angka = dua_angka.split(' ')

print(angka)
if angka[0] >= angka[1]:
      print(f'Nilai angka kedua akan mendekati angka pertama jika dikalikan dengan {int(angka[0]) // int(angka[1])}')
elif angka[1] <= angka[0]:
      print(f'Nilai angka pertama akan mendekati angka kedua jika dikalikan dengan {int(angka[1]) // int(angka[0])}')
else :
      print('  ')
