def yeni_katilimci():
    # file check
    # with open(file="MuhendisFest2024-Katılımcılar.txt", mode="a", encoding="utf-8") as newPart:
    #     pass

    print("Yeni katılımcı bilgilerini giriniz. ")
    print("Katılımcı Adı,Katılımcı Soyadı,Katılımcı ID (6 Haneli),Katılımcı Doğum ayı (1-12)")

    # Bütün Veri Girişi Kontrolü
    while True:
        pack = input("Bilgileri sırasıyla girin: ").lower().split(",")
        if len(pack) == 4:
            # ID'yi başa al
            pack.insert(0, pack.pop(2))
            break
        else:
            print("\nLütfen virgülle ayırarak 4 adet veri girin.")

    # Veri kontrol noktaları (1,2,3,4,5)
    # 1- Name check
    typeCheckName = pack[1]
    while True:
        try:
            typeCheckName = int(typeCheckName)

        except ValueError:
            pack[1] = typeCheckName
            break
        else:
            print("Lütfen ismini harf kullanarak gir: ")
            typeCheckName = input("İsim: ")

    # 2- Surname check
    typeCheckSurname = pack[2]
    while True:
        try:
            typeCheckSurname = int(typeCheckSurname)

        except ValueError:
            pack[2] = typeCheckSurname
            break
        else:
            print("Lütfen soyismini harf kullanarak gir: ")
            typeCheckSurname = input("Soyisim: ")

    # 3- ID integer check
    digitCheck = pack[0]
    while True:
        try:
            digitCheck = int(digitCheck)
            if len(str(digitCheck)) == 6:
                pack[0] = digitCheck
                break
            else:
                digitCheck = input("Lütfen 6 haneli bir ID belirle: ")

        except ValueError:
            digitCheck = input("Lütfen ID'yi sayı olarak gir: ")    

    # 4- ID check
    search = pack[0]
    while check_ID(search) == True:
        print("Bu ID kullanılmış.")
        search = input("Lüfen yeni bir ID belirleyin: ")
        check_ID(search)
    pack[0] = search

    # 5- month integer check
    typeCheckMonth = pack[3]
    while True:
        try:
            typeCheckMonth = int(typeCheckMonth)
            if typeCheckMonth < 1 or typeCheckMonth > 12:
                typeCheckMonth = input("Lütfen doğum ayını 1 ile 12 arasında gir: ")
            else:
                pack[3] = typeCheckMonth
                break
        except ValueError:
            typeCheckMonth = input("Lütfen doğum ayını 1 ile 12 arasında sayı olarak gir: ")

    print(pack)

    # with open("test.txt", mode="a", encoding="utf-8" ) as writeFile:
    #     for data in pack:
    #         writeFile.write(f"{data}\n")


# - Kullanıcıdan alınan bilgiler, dosyaya herhangi bir veri kaybı yaşanmadan ve dosya formatına uygun bir şekilde eklenmelidir.
# - Kullanıcıdan istenilen bilgiler:
# - Katılımcı Adı, Katılımcı Soyadı, Katılımcı ID ve Katılımcı Doğum ayı (1-12)
# - Daha önce kullanılan bir ID bir başka kullanıcı tarafından kullanılamaz.
# - Veri eklerken dikkatli dosya yazımı için `try/except` kullanılmalıdır.

def check_ID(search):
    with open("test.txt", mode="r", encoding="utf-8") as readFile:
        check = search
        while True:
            id = readFile.readline().rstrip()
            if id == check:
                return True
            elif id == "":
                return False

def check_digit():
    pass
def check_name():
    pass
def check_surname():
    pass
def check_month():
    pass


def katilimci_getir():
    pass
# - ID’si girilen katılımcının tüm bilgileri ekranda gösterilecektir.
#  - Dosya okuma işlemleri sırasında, girilen ID'ye ulaşılana kadar okuma yapılmalı ve bulunduğunda
# diğer kayıtlar okunmamalıdır

def girisKodu_sifre_uret():
    pass

# d) Elde edilen giriş kodları ve şifreler ayrı ayrı listelerde saklanacaktır.
# e) Dosya okuma işlemleri sırasında tüm metin küçük harfe dönüştürülecektir.
# Katılımcı bilgileri işlenirken her biri için benzersiz giriş kodu ve güvenlik şifresi oluşturulacaktır:

# f) Giriş kodu oluşturma adımları:
# - İsim ve soyisimden elde edilen değerler üzerinde işlemler yapılırken boşluklar kaldırılacaktır.
# - Adım1: İsmin ilk harfi ve soyismin son harfi alınacaktır. (örn: “John Doe”, “Je”)
# - Adım2: Katılımcının id’si ve katılımcının doğum ayı çarpılacak ve bu çarpım, katılımcı id’sinin
# ilk iki rakamı ile birleştirilecektir (örnek: 25 (katılımcı id) * 5 (doğum ayı) = 125, katılımcı id ilk iki
# rakamı 25: sonuç 25125).
# - Adım3: Giriş kodu, bu değerlerin kombinasyonu ile oluşturulacak (örn: “Je” + “25125” =
# Je25125).
# - Adım4: Oluşturulan giriş kodları listeye eklenir.

# g) Tüm giriş kodları ve şifreler, son aşamada “girisKodu_sifre.txt” dosyasına id, giriş_kodu,
# güvenlik_sifresi formatında kaydedilir.

def anlik_uret():
    pass

# 4. Kullanıcı girdisi ile anlık giriş kodu ve güvenlik şifresi üretmek için anlik_uret fonksiyonu
# hazırlanacaktır:

yeni_katilimci()
