#4 adalah 100 dalam biner dan 11 adalah 1011

x = 4
y = 11

print('biner dari', x,'adalah',format(x, '08b'))
print('biner dari', y,'adalah',format(y, '08b'))

#a. 4|11
print('*****************(4|11)******************')
print('biner dari', x,'adalah',format(x, '08b'))
print('biner dari', y,'adalah',format(y, '08b'))
print('=================================(|)')
print('nilai ', x|y,'angka binernya adalah ', format(x|y, '08b'))

#b. 4>>11
print('*****************(4>>11)*****************')
print('biner dari', x,'adalah',format(x, '08b'))
print('biner dari', y,'adalah',format(y, '08b'))
print('=================================(>>)')
print('nilai ', x>>y,'angka binernya adalah ', format(x>>y, '08b'))

#c. 4^11
print('*****************(4^11)*****************')
print('biner dari', x,'adalah',format(x, '08b'))
print('biner dari', y,'adalah',format(y, '08b'))
print('=================================(^)')
print('nilai ', x^y,'angka binernya adalah ', format(x^y, '08b'))

#d. ~4
print('*****************(~4)*****************')
print('biner dari', x,'adalah',format(x, '08b'))
print('biner dari', y,'adalah',format(y, '08b'))
print('=================================(~)')
print('nilai ', ~x,'angka binernya adalah ', format(~x, '08b'))

#e. 11&4
print('*****************(11&4)*****************')
print('biner dari', x,'adalah',format(x, '08b'))
print('biner dari', y,'adalah',format(y, '08b'))
print('=================================(&)')
print('nilai ', y&x,'angka binernya adalah ', format(y&x, '08b'))