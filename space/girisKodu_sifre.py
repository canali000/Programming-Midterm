def yeni_katilimci():
    print("Yeni katılımcı bilgilerini giriniz. ")
    print(
        "Katılımcı Adı,Katılımcı Soyadı,Katılımcı ID (6 Haneli),Katılımcı Doğum ayı (1-12)"
    )

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
    pack[1] = check_name(pack[1])

    # 2- Surname check
    pack[2] = check_surname(pack[2])

    # 3- ID digit check
    pack[0] = check_digit(pack[0])

    # 4- ID exist check
    search = str(pack[0])
    while check_ID(search) == True:
        print("Bu ID kullanılmış.")
        search = input("Lüfen yeni bir ID belirleyin: ")
        search = check_digit(search)
        check_ID(search)
    pack[0] = search

    # 5- month integer check
    pack[3] = check_month(pack[3])

    print(pack)

    with open(
        "MuhendisFest2024-Katılımcılar.txt", mode="a", encoding="utf-8"
    ) as writeFile:
        for data in pack:
            writeFile.write(f"{data}\n")


def katilimci_getir():
    """Kullanıcıdan ID alarak katılımcı bilgilerini ekrana yazar."""

    search = input("Katılımcının ID'sini gir: ")
    search = check_digit(search)
    dataPack = katilimci_bul(search)

    if dataPack == False:
        print("Katılımcı festival listesinde bulunamadı.")
    else:
        id = dataPack[0]
        isim = dataPack[1]
        soyisim = dataPack[2]
        ay = dataPack[3]

        print("İsim:", isim.title())
        print("Soyisim:", soyisim.title())
        print("Doğduğu ay:", ay)
        print("ID:", id)


def girisKodu_sifre_uret(id):
    """Her kullanıcı için bir şifre/giriş kodu üretir. Bunları "girisKodu_sifre.txt" dosyasında saklar."""
    data = katilimci_bul(id)
    print(data)
    # ['123456', 'ali', 'bilgin', '1']
    # ["000000", "can ali", "bilgin", "12"]
    ilkHarf = data[1][0]
    sonHarf = data[2][-1]
    id = data[0]
    ay = data[3]
    key = str(int(id) * int(ay))
    twoDigit = id[0] + id[1]
    combine = ilkHarf + sonHarf + twoDigit + key
    return combine


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
    """
    Kullanıcının isteğiyle anlık olarak şifre üretir.
    Böylece kullanıcı kendi şifresini görüntüleyebilir.
    """


# 4. Kullanıcı girdisi ile anlık giriş kodu ve güvenlik şifresi üretmek için anlik_uret fonksiyonu
# hazırlanacaktır:


def check_name(typeCheckName):
    """İsmin harf olarak girilmesini denetler."""

    while True:
        try:
            int(typeCheckName)
        except ValueError:
            return typeCheckName
        else:
            print("Lütfen ismini harf kullanarak gir.")
            typeCheckName = input("İsim: ")


def check_surname(typeCheckSurname):
    """Soyismin harf olarak girilmesini denetler."""

    while True:
        try:
            int(typeCheckSurname)

        except ValueError:
            return typeCheckSurname
        else:
            print("Lütfen soyismini harf kullanarak gir.")
            typeCheckSurname = input("Soyisim: ")


def check_ID(search):
    """Girilen ID'nin katılımcı listesinde olup olmadığını kontrol eder. True/False döndürür."""
    with open(
        "MuhendisFest2024-Katılımcılar.txt", mode="r", encoding="utf-8"
    ) as readFile:
        check = search
        for id in readFile:
            id = id.rstrip()
            if id == check:
                return True
        return False


def check_digit(digitCheck):
    """Girilen ID'nin 6 haneli bir sayı olmasını denetler."""
    while True:
        try:
            int(digitCheck)
            if len(digitCheck) == 6:
                return digitCheck
            else:
                digitCheck = input("Lütfen 6 haneli bir ID gir: ")

        except ValueError:
            digitCheck = input("Lütfen ID'yi sayı olarak gir: ")


def check_month(typeCheckMonth):
    """Ay bilgisinin 1 ile 12 arasında bir sayı olmasını denetler."""
    while True:
        try:
            typeCheckMonth = int(typeCheckMonth)
            if typeCheckMonth < 1 or typeCheckMonth > 12:
                typeCheckMonth = input("Lütfen doğum ayını 1 ile 12 arasında gir: ")
            else:
                return str(typeCheckMonth)

        except ValueError:
            typeCheckMonth = input(
                "Lütfen doğum ayını 1 ile 12 arasında sayı olarak gir: "
            )


def katilimci_bul(search):
    """
    Katlımcının ID'sinin bulunduğu yere kadar dosyayı okur.
    Daha sonra ID'ye bağlı diğer verileri okur.
    """
    with open(
        "MuhendisFest2024-Katılımcılar.txt", mode="r", encoding="utf-8"
    ) as readFile:
        dataPack = []
        for row in readFile:
            id = row.rstrip()
            if id == search:
                dataPack.append(id)
                for i in range(0, 3):
                    data = readFile.readline().rstrip()
                    dataPack.append(data)
                return dataPack  # diğer kayıtların okunmaması için döngü sonu
    return False



girisKodu_sifre_uret("222222")