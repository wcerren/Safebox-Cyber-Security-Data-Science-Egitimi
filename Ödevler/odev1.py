def kullanici_kayit():
    kullanici_bilgi = {}
    kullanici_adi = input("Kullanici adını girin")
    kullanici_sifre = input("Kullanici sifresini girin")
    kullanici_bilgi["kullanici_adi"]=kullanici_adi
    kullanici_bilgi["kullanici_sifre"]=kullanici_sifre
    with open("kullanici_bilgileri.txt","a") as f:
        f.write(kullanici_bilgi["kullanici_adi"]+","+kullanici_bilgi["kullanici_sifre"]+"\n")
    print("kullanıcı kayıt edildi")

def giris():
    kullanici_adi = input("Kullanıcı adını girin: ")
    kullanici_sifre = input("Kullanıcı şifresini girin: ")

    with open("kullanici_bilgileri.txt", "r") as f:
        for line in f:
            kullanici, sifre = line.strip().split(",")
            if kullanici == kullanici_adi and sifre == kullanici_sifre:
                print("Giriş yapıldı")
                return

    print("Bilgiler yanlış veya kullanıcı bulunamadı")


while True:
    secim = int(input("1-Kayıt, 2-Giriş, 3-Çıkış: "))

    if secim == 1:
        kullanici_kayit()
    elif secim == 2:
        giris()
    elif secim == 3:
        print("Çıkış yapılıyor")
        break
    else:
        print("Yanlış seçim yaptınız")


while True:
    secim = int(input("1-Kayıt,2-Giriş,3-Çıkış"))
    
    if secim == 1:
        kullanici_kayit()

    elif secim == 2:
        #Burası sizde
        pass
    elif secim == 3:
        print("Çıkış yapılıyor")
        break
    else:
        print("Yanlış seçim yaptınız")