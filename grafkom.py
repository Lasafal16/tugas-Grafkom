import numpy as np
import matplotlib.pyplot as grafik

x1 = int(input('Masukan nilai x1  : '))
y1 = int(input('Masukan nilai y1  : '))
x2 = int(input('Masukan nilai x2  : '))
y2 = int(input('Masukan nilai y2  : '))

print('=====================================================')

x = x1
y = y1

if x1 == x2:
    titik_A = []
    titik_B = []
    for i in range(0, y2, 1):
        print('Garis yang di lewati oleh titik A da titik B yaitu', x, ',', y+i)
        titik_A.append(x)
        titik_B.append(y+i)
    grafik.plot(titik_A, titik_B)
    grafik.show()

elif y1 == y2:
    titik_A = []
    titik_B = []
    for i in range(0, x2, 1):
        print('Garis yang di lewati oleh titik A dan B yaitu', x+i, ',', y)
        titik_A.append(x+i)
        titik_B.append(y)
    grafik.plot(titik_A, titik_B)
    grafik.grid()
    grafik.show()
