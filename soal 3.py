#berat_max = 50 lbs, 1 lbs = 0,45 kg
berat_max = 50 * 0.45
print('Berat maksimum dalam kg adalah ',berat_max, 'kg')
soalA = 110
soalB = 49

hasil1 = soalA < berat_max
hasil2 = soalB < berat_max
print('Jika berat maksimum adalah', berat_max,'kg, maka dengan berat lebih 110 kg, hasilnya menjadi ', hasil1,)
print('Jika berat maksimum adalah', berat_max,'kg, maka dengan berat 49 kg, hasilnya menjadi ', hasil2,)