def yeni_katilimci():
    with open(file="MuhendisFest2024-Katılımcılar.txt", mode="a", encoding="utf-8") as newPart:
        pass
    while True:
        print("Yeni katılımcı bilgilerini giriniz. ")
        print("Katılımcı Adı,Katılımcı Soyadı,Katılımcı ID,Katılımcı Doğum ayı (1-12)")
    
        # buraya input eklenecek 
        pack = input("Bilgileri sırasıyla girin: ").lower().split(",")
        
        # ID başa al
        pack.insert(0, pack.pop(2))
        
        with open("test.txt", mode="r", encoding="utf-8") as readFile:
            dataPack = readFile.readlines()
        
        for i in range(len(dataPack)):
            dataPack[i] = dataPack[i].rstrip()


        with open("test.txt", mode="a", encoding="utf-8" ) as writeFile:
            for data in pack:
                writeFile.write(f"{data}\n")

