"""Tugas Grafika Komputer
Membuat garis dengan algoritma brute force 
E1E120048 Safal
E1E120082 Muhamad Ikhwan
E1E120068 Febriansyah
E1E120020 Sri Adiningsih
E1E120094 Syarifah Nurhafni Ahmad """

import numpy as np
import matplotlib.pyplot as grafik

x1 = int(input('Masukan nilai x1  : '))
y1 = int(input('Masukan nilai y1  : '))
x2 = int(input('Masukan nilai x2  : '))
y2 = int(input('Masukan nilai y2  : '))

print('=====================================================')

x = x1
y = y1

#----kondisi dimana jika x1==x2
if x1 == x2:
    titik_A = []
    titik_B = []
    for i in range(0, y2, 1):
        print('Garis yang di lewati oleh titik A da titik B yaitu', x, ',', y+i)
        titik_A.append(x)
        titik_B.append(y+i)
    grafik.plot(titik_A, titik_B)
    grafik.show()
    
#------kondisi dimana jika y1=y2
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
    
#-----kondisi jika tidak terpenuhi
else:
    titik_A = []
    titik_B = []
    m_gradiengaris = (y2 - y1) / (x2 - x1)
    N = x2 - x1 + 1
    for i in range (0,N,1):
        nilai_y = m_gradiengaris * (x - x1) + y1
        ya = round(nilai_y)
        print('Garis yang di lewati oleh titik A da titik B yaitu ', x,',', ya)
        titik_A.append(x)
        titik_B.append(ya)
        x+=1
        
    grafik.plot(titik_A,titik_B)
    grafik.show()
