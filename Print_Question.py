#1-)Print fonksiyonu kullanimi nedir
'''print("merhaba") seklinde kullanilir'''
#2-)Birden fazla degeri ayni satirda yazdirmak icin print fonksiyonunda nasil kullanilmalidir
'''
deger1 ="soru 1"
deger2 ="soru 2"
print("birinci deger\t"+deger1+"\nikinci deger\t"+deger2) seklinde birden fazla degeri yazdirabiliriz
'''
#3-)print fonksiyonun varsayilan ayrac degeri nedir
'''
deneme ="amasya,nevsehir,ankara,manisa"
print(deneme.split(",")) seklinde ayirabilir ancak tam olarak dogrumu bilemedim
'''
#4-)Print fonksiyonu ile farkli turlerdeki verileri nasil bir arada yazdirabiliriz
'''
deger="string yazalim"
sayi=15
print("bu taraf string",deger,"bu taraf int",sayi) seklinde int ve stringi bir arada yazdirabiliriz
'''
#5-)print fonksiyonu icinde end ne ise yarar
'''print("deneme yazisidir end ne ise yarar",end="")
print("deneme devam ediyor") ornekten anladigim kadariyla alt satira gecmek yerine devam ettiriyor
bir nevi satir sonu karakteri yerine geciyor'''
#6-)Bir metni tersten nasil yazdiririz
'''metin="deneme"
print(metin[::-1]) bu kod sisteminde index uzerinden siralama yapiyoruz metin[::-1] diyerek aslinda 
metindeki string ifadenin indekslerini tersten okutuyoruz.Bu durumdada metini ters cevirmis oluyoruz.'''
#7-)Print fonksiyonu kullanarak bir degiskenin degerini ekrana yazdirmak icin hangi yontemi kullanabiliriz?
'''degisken="degiskenin degeerini ekrana yazdiralim"
x=10
print(degisken,x) seklinde degiskenleri ekrana yazdirabiliriz. '''
#8-)Print fonksiyonu ile sayilari ekrana belirli bir formatta yazdirmak icin hangi yontem kullanilir?
'''sayi=15
sayi=float(sayi)
print(sayi) belirli bir formattan anladigim kadariyla degisken int turundeyken floata cevirme olarak algiladim.'''
#9-)bir satiri bos birakmadan iki print fonksiyonu kullanarak nasil bir cikti elde edersiniz?
'''print("merhaba");print("sanada merhaba")'''
#10-)bir liste veya tuple icindeki ogeleri sirasiyla yazdirmak icin print fonksiyonu icinde nasil bir ifade kullanilir?
'''Deneme_tuple=["1","4","3","2","6"] #== Tuple olusturma sekli
Deneme_tuple.sort()
print(Deneme_tuple)'''