# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:12:55 2019

@author: isil
"""

import math
import statistics 

dizi = []
num = int(input("kac elemanli dizi gireceksiniz:")) #dizi olustur
print ("sayilari giriniz:")

for i in range(num):
    n = input("sayi:")
    dizi.append(int(n)) #kullanicidan diziye eleman ekle
    
toplam = 0
ortalama = 0

for num in range(0, len(dizi)): #dizinin elemanlarinin toplamini bul
    toplam += dizi[num] 

ortalama = toplam / len(dizi) #dizinin ortalamasini bul
print(ortalama)

hesap = 0
for i in range(0 , len(dizi)):    
    hesap = hesap +((abs(dizi[i]-ortalama))**2) #standart sapma formulunu icin toplamfark sembolu
print(hesap)
    
    
formul = math.sqrt((1/(len(dizi)-1)*hesap)) #genel standart sapma hesabi

print("sonuc:", formul) # adim adim islenen sonuc

print("Kutuphane kullanilarak bulunan cozum: % s " % (statistics.stdev(dizi))) #standart sapma metodu ile bulunan direkt cozum 
