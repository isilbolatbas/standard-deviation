# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 00:35:24 2019

@author: isil
"""

from dizi import formul, ortalama, dizi

print("1-dizinin max elemani")
print("2-dizinin min elemani")
print("3-dizinin ortalamasi")
print("4-dizinin standart sapmasi")

secim = int(input("islem yapmak istediginiz durumu seciniz"))

if secim == 1:
    print ("dizinin en buyuk elemani", max(dizi))
elif secim == 2:
    print("dizinin en kucuk elemani", min(dizi))
elif secim == 3:
    print("dizinin ortalamasi", ortalama)
else:
    print("dizinin standart sapmasi", formul)
    
    

