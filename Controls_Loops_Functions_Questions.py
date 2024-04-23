import time
#1-)Kullanicidan alinan sayinin tek mi cift mi oldugunu kontrol eden kodu yaziniz.
'''Numb=int(input("bir sayi giriniz"))
if( Numb % 2 == 0):
    print("sayi cifttir")
else:
    print("sayi tektir")'''

#2-)Kullanicadan alinan sayinin tersini alan kodu yaziniz.
'''a=int(input("bir sayi giriniz"))
if(a>0):
    a = a * (-1)
    print(a)
else:
    a = a * (-1)
    print(a)'''
#3-)Kullanicidan bir vize ve bir final notu isteyiniz.Eger vize ve final notu 0 ile 100 arasinda
# degilse ekrana hata mesaji veriniz.Eger 0 ile 100 arasinda ise not ortalamasinin %40 ni ile final
# notunun %60 nin toplami olarak hesaplayip ekranda yazdiriniz. Ardindan not ortalamasini asagidaki kurala
# gore hesaplayip ekrana yazdiriniz.
#0<= not < 60  ise F
#60<= not < 70  ise D
#70<= not < 80  ise C
#80<= not < 90  ise B
#90<= not < 100  ise A
'''viz=int(input("bir vize puani giriniz"))
fin=int(input("bir final puani giriniz"))
result=(viz*0.4)+(fin*0.6)
if(result<=100 and result>=90):
    print("A")
elif(result<90 and result>=80):
    print("B")
elif(result<80 and result>=70):
    print("C")
elif(result<70 and result>=60):
    print("D")
elif(result<60 and result>=0):
    print("F")
else:
    print("hatali islem")'''
#4-)Kullanicidan ucgen  dikdortgen kare secmesini isteyiniz. Ardindan secim yanlissa hata mesaji veriniz.
# Uygun sekilde secim yapilmissa secilen sekle gore kenar uzunluklarini isteyiniz ardindan  alan  ve cevre
# degerlerini hesaplayiniz.
'''secim=input("Lutfen secim yapiniz Ucgen=1,Kare=2,Dikdortgen=3\n")
if(secim=="1"):
    yukseklik=int(input("Ucgen alani icin taban giriniz\n"));taban=int(input("ucgen icin yukseklik giriniz\n"));
    alan1=int((yukseklik*taban)/2)
    print("Ucgeninizin alani:",alan1)
elif(secim=="2"):
    kenar=int(input("Kare icin kenar giriniz\n"));
    alan2=kenar**2
    print("Karenizin alani:\n",alan2)
elif(secim=="3"):
    kenar1=int(input("Dikdortgen alani icin  kenar giriniz\n"));kenar2=int(input("Dikdortgen icin  kenar giriniz\n"))
    alan3=kenar1 * kenar2
    print("Dikdortgeninizin alani:\n",alan3)
else:
    print("hatali tuslama yaptiniz")'''
#5-) Kullanicidan iki sayi isteyiniz sonrasinda yapilmak istenilen islemi isteyiniz (carpma,bolme,toplama, cikarma).
# Sonrasinda islemi yapip sonucu ekrana yazdiriniz.
'''Numb1=int(input("1.sayiyi giriniz:\n"))
Numb2=int(input("2.sayiyi giriniz:\n"))
islem=int(input("Lutfen yapmak istediginiz islemi giriniz:1-Carpma,2-Bolme,3-Toplama,4-Cikarma\n"))
def Sum(Numb1,Numb2):
    result=Numb1 + Numb2
    return result
def Mult(Numb1,Numb2):
    result=Numb1*Numb2
    return result
def Div(Numb1,Numb2):
    result=Numb1/Numb2
    return result
def Sub(Numb1,Numb2):
    result= Numb1-Numb2
if(islem==1):
    print("islem sonucunuz:",Mult(Numb1,Numb2))
elif(islem==2):
    print("islem sonucunuz:",Div(Numb1, Numb2))
elif(islem==3):
    print("islem sonucunuz:",Sum(Numb1,Numb2))
elif(islem==4):
    print("islem sonucunuz:",Sub(Numb1, Numb2))
else:
    print("hatali islem")'''
#6-)6- Bir 4 haneli pin kodu belirleyiniz. Bu pin kodunu uygulamaniza kisiyi dogrulamakta kullanmak icin kullancaksiniz.
# Kullanici 3 kez yanlis pin girdiginde uyari mesaji vererek uygulamayi sonlandirir. Basarili giriste ise "Giris dogrulandi"
# seklinde ekrana bildirim versin.
'''python
pin="1234"
Pass=input("Lutfen sifreyi giriniz:")
for Hak in range(3,0,-1):
    if (Pass != pin and len(Pass) != 4 and Pass.isalpha() != True and Hak >= 0):
        print("Lutfen 4 haneli sifreyi giriniz.Kalan hakkiniz {}".format(Hak))
        Pass = input("sifre giriniz :\n")
    elif (Pass != pin and len(Pass) == 4 and Pass.isalpha() == True and Hak >= 0):
        print("Lutfen rakam giriniz.Kalan hakkiniz {}".format(Hak))
        Pass = input("sifre giriniz :\n")
    elif (Pass != pin and len(Pass) != 4 and Pass.isalpha() == True and Hak >= 0):
        print("Lutfen rakam giriniz.Kalan hakkiniz {}".format(Hak))
        Pass = input("sifre giriniz :\n")
    elif (Pass != pin and len(Pass) == 4 and Pass.isalpha() != True and Hak >= 0):
        print("Lutfen tekrar giriniz.Kalan hakkiniz {}".format(Hak))
        Pass = input("sifre giriniz :\n")
    elif(Pass == pin and len(Pass) == 4 and Pass.isalpha() != True and Hak >= 0):
        print("Giris Basarili ")
        time.sleep(1)
        print("Cikis yapildi.")
        break
time.sleep(1)
print("3 kere yanlis girdiniz,Cikis yapildi.")'''
#7-)7- Kullanicidan bir sayi girilmesi istinilsin ekran girilen sayiya kadar olan sayilar yazdirilsin.
'''Say=int(input("Bir sayi giriniz:\n"))
for i in range(Say,0,-1):
    i=i-1
    print(i)'''
#8-)Kullanicidan alt limit ust limit ve artis miktari istenilsin.Ekran alt limitten baslayarak artis
# miktari kadar artirarak ust limite kadar sayilar ekrana yazdirilsin.
'''Alt_limit=int(input("Alt limit giriniz"))
Ust_limit=int(input("Ust limit giriniz"))
Artis=int(input("Artis miktari giriniz"))
for Alt_limit in range(Alt_limit,Ust_limit+1,Artis):
    print(Alt_limit)'''
#9-)Kullanicidan alt limit ve ust limit alinsin ve aradaki sayilarin toplami hesaplansin.
'''Alt_limit=int(input("Alt limit giriniz"))
Ust_limit=int(input("Ust limit giriniz"))
Artis=int(input("Artis miktari giriniz"))
sonuc=0
for Alt_limit in range(Alt_limit,Ust_limit+1,Artis):
    if(Alt_limit<=Ust_limit):
        sonuc+=Alt_limit
print(sonuc)'''
#10-)Girilen sayinin asal olup olmadigini kontrol edip asalsa "Bu bir asal sayidir" degilse "Asal sayi degildir" seklinde
# ekrana mesaj yaziniz.
'''Sayi=int(input("Bir sayi giriniz:\n"))
if(Sayi%2==0):
    print("Asal sayidir")
else:
    print("Asal sayi degildir")'''
#11-)-Girilen metnin tersten ve duzden birbirine esit olup olmadigini kontrol eden kodu yaziniz.
# Ornek:
# abcba == polindromdur
# deded == polindromdur
# dead  != polindrom degildir
'''Met=input("Bir metin giriniz:\n")
if(Met==Met[::-1]):
    print("Polindromdur")
else:
    print("Polindrom degildir.")'''
#12-)Girilen sayinin faktoriyelini hesaplayan kodu yaziniz eger deger sifirdan kucukse hata mesaji verin
'''Numb=int(input("bir sayi giriniz:\n"))
b=1
if(Numb>=0):
    for Numb in range(Numb, 0, -1):
        b *= Numb
    print(b)
else:
    print("Hata")'''
#13-)Girilen sayinin tum pozitif bolenlerini bulunuz.
'''a=int(input("Bir sayi giriniz"))
b=a
while(a>0 and b>0):
    if(a % b == 0):
        print(f"{b},{a} bolenidir ")

    else:
        print(f"{b},{a} boleni degildir.")
    b-=1'''





