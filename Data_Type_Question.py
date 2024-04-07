#VERI TURLERI SORULARI
#1-) Number: Bir sayıyı iki ile çarpan Python ifadesi nedir?
'''sayi=int(input("sayi giriniz:"))*2
print(sayi)'''
#2-) String: Bir metni tersten yazan Python kodu nedir?
'''metin="metini tersten yazicak"
print(metin[::-1])'''
#3-[) List: Bir liste içindeki elemanları tersine çeviren Python kodunu yazın.
'''sehirler=["amasya","ankara","istanbul"]
print(sehirler[::-1])'''
#4-)Tuple: Bir demeti oluşturan ve içinde "apple" ve "orange" olan bir Python ifadesi nedir?
'''meyvelere="apple","orange"
meyvelere=tuple(meyvelere)
print(meyvelere)'''
#5-) Dictionary: Bir sözlükteki belirli bir anahtarın karşılık gelen değerini güncelleyen Python kodu nedir?
'''kelimeler_dic=dict(sol="left",sag="right")
print(kelimeler_dic)
kelimeler_dic["sol"]='lefto'
print(kelimeler_dic)'''
#6-) Sets: İki kümenin birleşimini bulan Python kodunu yazın.
'''sayilar={"1","2","3"}
sayilar2={"4","5"}
sayi=sayilar.union(sayilar2)
sayi=list(sayi)
sayi.sort()
print(sayi)'''
#7-)Number: Bir sayının karesini hesaplayan Python ifadesi nedir?7
'''sayi=int(input("sayi giriniz"))
def kare(sayi):
    return sayi**2
sonuc=kare(sayi)
print(sonuc)'''
#8-)String: Bir metinde belirlibir karakterin kaç kez geçtiğini sayan Python kodu nedir?
'''metin="bu karakter dizininde kac kere a kullanildigi sayilacak"
print(metin.count("a"))'''
#9-)List: Bir liste içinde belirli bir elemanın kaç kez geçtiğini sayan Python kodunu yazın.
'''liste=["amasya","amasya","amasya","amasya","amasya",]
print(liste.count("amasya"))'''
#10-)Tuple: Bir demette belirli bir değerin kaç kez geçtiğini sayan Python kodu nedir?
'''Sayilar=("2","5","4","5")
print(Sayilar.count("5")) tuple turunde oldugundan dolayi degistirilemiyor ancak veri turu izin verdiginden dolayi
count() vs islemleri yapabiliyoruz'''
#11-)Dictionary: Bir sözlükte belirli bir anahtarın var olup olmadığını kontrol eden Python kodunu yazın.
'''Hayvanlar=dict(kedi="mirnak",Kopek="garip",yilan="sirnasik",serce="cirtak")
Hayvanlar=list(Hayvanlar.keys())
print('yilan'in Hayvanlar)
print(type(Hayvanlar))  Dictionary tipinde olan veriler uzerinde siralama islemi yapilamayan ancak diger islemlere izin 
 veren bir veri turu oldugundan dolayi oncelikle liste turunde siralayip list(Hayvanlar.keys()) yardimiyla 
 anahtar kelimeleri liste turune cevirip sonrasinda count ile aradigimiz anahtarin sayisina bakarken var  olup
  'yilan' in Hayvanlar yazarakta boolen tipte veri donduruyoruz olmadigini '''
#12-)Sets: İki kümenin farkını bulan Python kodu nedir?
'''kume1={"1","2","3","4"}
kume2={"3","4","5","6"}
kume3=kume1.difference(kume2)
print(kume3)'''
#13-) List: Bir listeden belirli bir elemanı kaldıran Python kodu nedir?
'''liste1=["amasya","erzurum","Bodrum"]
liste1.remove("erzurum")
print(liste1) remove vs fonksiyonlari kullanirken oncelikle tekrar tanimlama yapip sonrasinda print etmemiz gerekmektedir
(sanirsam)'''
#14-)Tuple: İki demeti birleştiren Python ifadesi nedir?
'''demet1=("papatya","Menekse","Orkide")
demet2=("lotus","Kasimpati","Nilufer")
demet3=demet2 + demet1
tuple(demet3)
print(type(demet3))
print(demet3) '''
#15-) Bir sözlükten belirli bir anahtarı ve karşılık gelen değeri kaldıran Python kodu nedir?
'''sozluk1=dict(isim="mery",soyisim="gus",yetkinlik="cakma doktor")
del sozluk1["yetkinlik"]
print(sozluk1)  dictionary turundeki veriler sadece siralanamaz ancak diger islemler gerceklesebilir bu sebepden dolayi
del islemi ile istedigimiz key:value degerini silebiliriz'''
#16-)String: Bir metni başka bir metinle birleştiren Python kodunu yazın
'''metin1="deneme metnidir digeriyle birlestiricez"
metin2=" metinin devamidir metinler birlesti"
metin3=metin1 + metin2
print(metin3)'''
#17-) Set:İki kümenin kesişimini bulan Python kodu nedir
'''set1={"deneme","deneme2","deneme3"}
set2={"deneme4","deneme5","deneme2"}
print(set1.intersection(set2))
print(type(set1))'''
#18-)Number: Bir sayının karekökünü bulan Python ifadesi nedir?
'''Sayi=int(input("bir sayi giriniz:"))
def karekok(sayi):
    return sayi**(1/2)
print(int(karekok(Sayi))) tam sayi turunde cikti vermesi icin print ederken int cevirmesi yaptim'''
#19-)String: Bir metni belirli bir karakter göre ayıran Python kodunu yazın
'''Metin1="bu metini belli , bir karaktere gore ayiracagiz"
print(Metin1.split(","))'''
#20-)List: Bir liste içinde belirli bir elemanın indeksini bulan Python kodu nedir?
'''Emotions=["smile","sad","angry"]
print(Emotions.index("sad"))'''
#21-)Tuple: Bir demeti belirli bir değere göre filtreleyen Python kodu nedir?
'''Tuple1=("1","6","3")
Tuple1=list(Tuple1)
print(Tuple1[0])
print(type(Tuple1))'''
#22-) Dictionary: Bir sözlükteki tüm anahtarları listeleyen Python kodu nedir?
'''meyveler=dict(elma="apple",portakal="orange",uzum="grapes")
print(meyveler.keys())
print(type(meyveler))'''
#23-)Sets: Bir kümenin boş olup olmadığını kontrol eden Python kodunu yazın.
'''Kume1={"ahmet","mehmet"}
print(len(Kume1))
print(type(Kume1))'''
#24-)Number: İki sayının farkını bulan Python ifadesi nedir?
'''x=int(input("Birinci sayiyi giriniz"))
y=int(input("ikinci sayiyi giriniz"))
def fark(x,y):
    return x-y
print(fark(x,y))'''
#25-)String: Bir metnin uzunluğunu bulan Python kodu nedir?
'''Metin=str(input("bir metin giriniz uzunlugunu  bulalim:"))
print(len(Metin))'''
#26-)List: Bir listedeki en büyük elemanı bulan Python kodunu yazın
'''List1=list(input("bir liste giriniz"))
List1.sort()
List1.reverse()
print(List1[0])'''
#27-)Tuple: İki demeti çarpan Python ifadesi nedir?
'''Tuple1=("1","2")
Tuple2=("3","4")
Tuple2=list(Tuple2)
Tuple1=list(Tuple1)
for i in Tuple1:
    for j in Tuple2:
        i=int(i)
        j=int(j)
        result=i*j
        print(result)'''
#28-)Dictionary: Bir sözlüğe yeni bir anahtar ve değer ekleyen Python kodu nedir?
'''dict1=dict(meyve="elma")
print(dict1)
dict1.update(Hayvan="ari")
print(dict1)'''

