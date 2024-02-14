import math

#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

def vucutİndeksi(boy, agirlik):
    vki = agirlik / (boy * boy)
    return vki

boy = float(input("Lütfen boyunuzu (metre cinsinde) giriniz: "))
agirlik = float(input("Lütfen kilonuzu giriniz: "))

vki = vucutİndeksi(boy, agirlik)

if vki <18:
    print("\nZayıf VKİ:{}".format(vki))
elif vki >= 18 and vki <25 :
    print("\nNormal VKİ:{}".format(vki))
elif vki >= 25 and vki <30:
    print("\nKilolu VKİ:{}".format(vki))
elif vki >= 30 and vki <35:
    print("\nObez VKİ:{}".format(vki))
else:
    print("\nCiddi obez VKİ:{}".format(vki))

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

def zamliMaas(maas, zamOrani):
    #zamMiktari = maas * (zamOrani / 100)
    zamliMaas = maas + (maas * zamOrani / 100)
    return zamliMaas

maas = float(input("Lütfen mevcut maaşı giriniz: "))
zamOrani = float(input("Lütfen zam oranını giriniz (Sadece pay kısmını giriniz ,payda kısmı 100 alınacaktır): "))

zamli = float (zamliMaas(maas, zamOrani))
print("Zamlı Maaş:", zamli)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

a = float(input("Birinci sayiyi giriniz:"))
b = float(input("İkinci sayiyi giriniz:"))
c = float(input("Üçüncü sayiyi giriniz:"))

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)
print("En buyuk sayi: ", maximum(a, b, c))
    
#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

def daireninAlani(yariCap):
    alan = yariCap ** 2 * math.pi
    return alan

def daireninCevresi(yariCap):
    cevre = 2 * math.pi * yariCap
    return cevre

yariCap = float(input("Yaricapi giriniz: "))

alan = daireninAlani(yariCap)
cevre = daireninCevresi(yariCap)

print("Dairenin Alanı:", alan)
print("Dairenin Çevresi:", cevre)

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.github'a ekleme yapalım, linkleri paylaşalım lütfen 🙂

##cozum (girilen sayının polindrom olup olmadığınıkontrol eder.)
def palindrom_mu(sayi):
    sayi_str = str(sayi)
    ters_sayi_str = sayi_str[::-1]
    return sayi_str == ters_sayi_str

sayi = input("Lütfen bir sayı giriniz: ")

if palindrom_mu(sayi):
    print(sayi, "bir palindromdur.")
else:
    print(sayi, "bir palindrom değildir.")

##cozum (girilen metnin polindrom olup olmadığınıkontrol eder.)
metin = input('Metni Girin : \n')
ters=metin[::-1]

print('Girilen metnin tersi = %s' % (ters)) ## %s string
if ters == metin:
    print('Girilen metin palindrom')
else:
    print('Girilen metin palindrom değil.')