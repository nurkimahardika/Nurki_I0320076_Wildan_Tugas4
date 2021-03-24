#Untuk mendaftar pada kursus online, calon siswa harus berusia minimal 21 tahun dan telah lulus ujian kualifikasi.

print('Berapakah umur anda?')
umur = (input('Umur : '))
print('Apakah anda sudah lulus ujian kualifikasi? (Ya / Tidak)')
jawab = (input('Jawab: '))

if umur >= '21' :
    if jawab == 'Ya'  :
        print('Anda dapat mendaftar kursus.')
    else :
        print('Anda tidak dapat mendaftar kursus.')

else :
    print('Anda tidak dapat mendaftar kursus.')