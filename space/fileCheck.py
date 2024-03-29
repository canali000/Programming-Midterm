try:
    with open("x.txt", "r", encoding= "utf-8") as checkFile:
        checkFile.read()
except FileNotFoundError:
    print("Katılımcı dosyası bulunamadı.")
    print("Yeni dosya oluşturuluyor.")
    with open("x.txt", "w",encoding=("utf-8")) as createFile:
        createFile.write("")