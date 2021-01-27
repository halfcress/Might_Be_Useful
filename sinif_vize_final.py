# Bir yapı tanımlanacaktır (Öğrenci no, Öğrenci Adı, Öğrenci Soyadı, Vize, Final, ortalama).
# Kullanıcıdan önce Sınıftaki Öğrenci sayısı girilmesi istenecektir(1).
# Sınıftaki Öğrencilerin no, adı ve soyadı girilecektir(2).
# Tüm sınıf no, ad, soyad girildikten sonra Öğrencinin no, ad, soyadı gösterilip vize notlarının girilmesi istenecektir(3).
# Ardından vizenin girildiği gibi final notlarının girilmesi istenecektir(4).
# %40 vize,  %60 final hesaplaması yapılarak ortalama alanına kaydedilip(5).
# Sınıftaki öğrencilerin no, ad, soyad ve ortalamaları ekrana gösterilecektir(6).
# İşlem sırası tanımlandığı sırayla gerçekleştirilecektir.

ogrenci_sayi = int(input("sınıftaki öğrenci sayısını giriniz"))

liste = []
ortalama_liste = []

for i in range(1,ogrenci_sayi+1):
    no = input("{}. öğrencinin numarasını giriniz: ".format(i))
    ad = input("{}. öğrencinin adını giriniz: ".format(i))
    soyad = input("{}. öğrencinin soyadını giriniz: ".format(i))

    liste.append((no,ad,soyad))

for i in liste:
    print("{} numaralı {} {} isimli öğrencinin vize ve final notları girilmelidir.".format(i[0],i[1],i[2]))
    vize = int(input("Vize notu: "))
    final = int(input("Final notu: "))
    ortalama = (vize*40)/(100) + (final*60)/(100)
    ortalama_liste.append(ortalama)

for i in range(ogrenci_sayi):
    print("No: {}, Ad: {}, Soyad: {}, Ortalama = {}".format(liste[i][0],liste[i][1],liste[i][2],ortalama_liste[i]))
