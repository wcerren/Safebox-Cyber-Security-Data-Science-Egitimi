def film_adi_kaydet():
    film_adi = input("Film adını girin: ")

    with open("filmler.txt", "a") as dosya:
        dosya.write(film_adi + "\n")

    print("Film adı kaydedildi.")


def film_adi_ara():
    aranacak_film = input("Aranacak film adını girin: ")

    with open("filmler.txt", "r") as dosya:
        bulundu = False
        for satir in dosya:
            if aranacak_film.lower() in satir.lower():
                print("Film bulundu:", satir.strip())
                bulundu = True

        if not bulundu:
            print("Aradığınız film bulunamadı.")


def film_adi_sil():
    silinecek_film = input("Silinecek film adını girin: ")

    with open("filmler.txt", "r") as dosya:
        film_listesi = dosya.readlines()

    with open("filmler.txt", "w") as dosya:
        silindi = False
        for satir in film_listesi:
            if silinecek_film.lower() not in satir.lower():
                dosya.write(satir)
            else:
                silindi = True

        if silindi:
            print("Film başarıyla silindi.")
        else:
            print("Silinecek film bulunamadı.")


while True:
    print("1 - Film adı kaydet")
    print("2 - Film adı ara")
    print("3 - Film adı sil")
    print("4 - Çıkış")

    secim = input("Bir seçenek girin (1/2/3/4): ")

    if secim == "1":
        film_adi_kaydet()
    elif secim == "2":
        film_adi_ara()
    elif secim == "3":
        film_adi_sil()
    elif secim == "4":
        break
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")

print("Program sonlandırıldı.")
