from islemler import yeni_katilimci, anlik_uret, katilimci_getir

def main():
    # MuhendisFest2024-Katılımcılar.txt dosyası kontrolü
    try:
        with open("MuhendisFest2024-Katılımcılar.txt", mode="r", encoding= "utf-8") as checkFile:
            checkFile.read()
    except FileNotFoundError:
        print("Katılımcı dosyası bulunamadı.")
        print("Yeni dosya oluşturuluyor.")
        with open("MuhendisFest2024-Katılımcılar.txt", mode="w",encoding=("utf-8")) as createFile:
            createFile.write("")

    # girisKodu_sifre.txt dosyası kontrolü
    try:
        with open("girisKodu_sifre.txt", mode="r", encoding= "utf-8") as checkFile:
            checkFile.read()
    except FileNotFoundError:
        print("Giriş kodları dosyası bulunamadı.")
        print("Yeni dosya oluşturuluyor.")
        with open("girisKodu_sifre.txt", mode="w", encoding=("utf-8")) as createFile:
            createFile.write("")

    end = False
    while not end:
        print()
        menu_goruntule()
        print()
        choice = input("Seçim: ")
        if choice == "1":
            yeni_katilimci()
        elif choice == "2":
            katilimci_getir()
        elif choice == "3":
            anlik_uret()
        else:
            print("Geçersiz Seçim")
        print()
        loop = input("Menüyü görüntülemek için 'y', çıkmak için 'n' girin: ")
        if loop == "n":
            end = True     

def menu_goruntule():
    print("Menu")
    print("-----")
    print("1- Yeni Katılımcı Ekle")
    print("2- Katılımcı Bilgilerini Görüntüle")
    print("3- Giriş Kodunu Görüntüle")
    print()
    print("Yapmak istediğin işlemi gir.")

if __name__ == "__main__":
    main()
