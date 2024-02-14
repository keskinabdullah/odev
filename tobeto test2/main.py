adınız=input("adınızı giriniz:")
kilo=int(input("kilonuzu giriniz:"))
boy=float(input("boyunuzu giriniz:"))
formül=kilo/(boy*boy)
print(adınız,",boy kilo endeksi sayısal değerin:",formül)
if 0<=formül<=18 :
    print("zayıf çıktın! KİLO ALMAN GEREKİYOR!")
elif 18<formül<=24:
    print("normal çıktın.İDEAL KİLODASIN.")
elif 24<formül<=29:
   print("fazla kilolu çıktın.KİLO VERMEN GEREKİYOR!")
else:
    print("İDEAL KİLONUN ÇOK ÜSTÜ ÇIKTIN...")

