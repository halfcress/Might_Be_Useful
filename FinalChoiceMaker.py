import os
import random

list = []
menu = """

1) Eleman Ekle
2) Sonucu Göster
3) Çık



"""
while True:

    os.system("cls")
    print(menu)
    secim = input("Yapmak istediğiniz işlemi giriniz: ")

    if secim == "1":
       x = str(input("Lütfen Eklemek İstediğiniz Elemanı Giriniz: "))
       list.append(x)

    elif secim == "2":
        karar = random.randint(0, len(list))
        print("{}".format(list[karar]))
        print("İşlem tamamlandı yeniden ana menü için Enter Tuşuna, Tüm listeyi görüntülemek için 'Z' Tuşuna ")
        print("Çıkmak için 'Q' Tuşuna basın.")

        x = str(input())
        if x == "q":
            quit()
        elif x == "z":
            print(list)
    if secim == "3":
        quit()







