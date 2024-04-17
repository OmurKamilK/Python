from functools import reduce
#1-)Bir sayinin faktoriyelini bulan rekursif fonksiyonu yaziniz.
'''def Fak(n):
    if n == 1 or n == 0:
        return  1
    else:
        return n * Fak(n-1)
a=int(input("Bir sayi giriniz:\n"))
res=Fak(a)
print(f"{a} sayisi faktoriyeli:{res}")'''
#2-)Gonderilen karakterleri bir bir azaltarak ekra na yazan rekursif fonsiyonnu yaziniz.
''''met=input("Bir kelime giriniz:\n")
def Ch(met):
    if(len(met)==0):
        return met
    else:
        print(met)
        Ch(met[:-1])
print(Ch(met))'''
#3-)Rekursif bir sekilde us alan fonksiyonu yaziniz.
'''a=int(input("Bir sayi giriniz:\n"))
b=int(input("sayinin ussunu giriniz:\n"))
def Ex(a,b):
    if b==0:
        return 1
    else:
        return a*Ex(a,b-1)
print(Ex(a,b))'''
#4-)Girilen sayiya gore fibonacci sirasindaki sayiyi veren fonksiyonu yaziniz
'''a=int(input("Bir sayi giriniz:\n"))
def Fb(a):
    if a<=1:
        return a
    else:
        return Fb(a-1)+Fb(a-2)
print(Fb(a))'''
#5-)Girilen yaziyi tersine ceviren rekursif fonksiyonu yaziniz.
'''Met=input("Bir metin giriniz")
def Rv(Met):
    if(len(Met)==0):
        return Met
    else:
        return Met[::-1]
print(Rv(Met))'''
#6-)Gonderilen listenin elemanlarinin ciftmi tekmi ekrana yazdiran `lambda` fonksiyonunu yaziniz.
'''sayi=int(input("Bir sayi giriniz"))
a=lambda sayi:print("even") if sayi%2==0 else print("odd")
print(a(sayi))'''
#7-) `lambda` fonksiyonu kullanarak toplama islemi yapan fonksiyonu yaziniz.
'''b=lambda c,d:c+d
print(b(5,6))'''
#8-)Gonderilen sayinin kare kokunu alan `lambda` fonksiyonunu yaziniz.
'''a=int(input("bir sayi giriniz:\n"))
b=lambda a:a**(1/2)
print(b(a))'''
#9-) Verilen listenin karekokunu hesaplayan map fonksiyonunu yaziniz.
'''sayilar = [1, 4, 9, 16, 25]
sq=lambda x:x ** (1/2)
print(map(sq,sayilar))
print(list(map(sq,sayilar)))'''
#10-)Verilen listedeki ifadeleri map fonksiyonu kullanarak buyuk harfe ceviriniz.
'''kelimeler = ['python', 'programlama', 'dili']
Up=lambda y: y.upper()
print(list(map(Up,kelimeler)))'''
#11-)Verilen listedeki kelimelerin harf sayisini bulunuz.
'''kelimeler = ['merhaba', 'dunya', 'python']
z=lambda x:len(x)
print(map(z,kelimeler))
print(list(map(z,kelimeler)))'''
#12-)Listenin elemanlarini toplayan `reduce` fonksiyonunu yaziniz.
'''liste = [1, 2, 3, 4, 5]
a=reduce(lambda x,y:x+y,liste)
print(a)'''
#13-)Listedeki buyuk elemani bulan `reduce` fonksiyonunu yaziniz


