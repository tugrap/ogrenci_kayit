def not_hesap(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenci_adi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = int((not1 + not2 + not3)/3)
    if ort>=90 and ort <=100:
        harf = "AA"
    elif ort >=85 and ort <=89 :
        harf = "BA"
    elif ort >=80 and ort <=84 :
        harf = "BB" 
    elif ort >=75 and ort <=79 :
        harf = "CB"
    elif ort >=70 and ort <=74 :
        harf = "CC"
    elif ort>=65 and ort <=69 :
        harf = "DC"
    elif ort >=60 and ort<=64 :
        harf = "DD"
    elif ort >=50 and ort <=59 :
        harf = "FD"
    else :
        harf = "FF"

    return ogrenci_adi + ": " +  harf + "\n"


def ort_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file :
        for satir in file:
            print(not_hesap(satir))

def not_gir():
    ad = input("ogrenci adi: ")
    soyad = input("ogrenci soyadi: ")
    not1 = input("ilk notu : ")
    not2 = input("ikinci notu : ")
    not3 = input("ucuncu notu : ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file :
        file.write(ad + " " + soyad+ " : " + not1+"," +not2+","+not3+"\n")

def kaydet():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file :
        liste = []

        for i in file:
            liste.append(not_hesap(i))
        
        with open("sonuclar.txt", "w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



while True:
    islem = input("1- notlari oku\n2- not gir\n3- Notlari kaydet\n4- Cikis\n")



    if islem == "1" :
        ort_oku()
    elif islem == "2" :
        not_gir()
    elif islem == "3" :
        kaydet()
    else :
        break

