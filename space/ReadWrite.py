print("Yeni katılımcı bilgilerini giriniz. ")
print("Katılımcı Adı,Katılımcı Soyadı,Katılımcı ID,Katılımcı Doğum ayı (1-12)")
pack = "can,bilgin,230601097,12".lower().split(",")

# ID başa al
pack.insert(0, pack.pop(2))

# with open("test.txt", mode="w", encoding="utf-8" ) as writeFile:
#     for data in pack:
#         writeFile.write(f"{data}\n")

with open("test.txt", mode="r", encoding="utf-8") as readFile:
    dataPack = readFile.readlines()

for i in range(len(dataPack)):
    dataPack[i] = dataPack[i].rstrip()


search = "230"
start = dataPack.index(search) 

id = dataPack[start]
isim = dataPack[start+1]
soyisim = dataPack[start+2]
ay = dataPack[start+3]

participants = {}
ozellik = {}

participants[id] = ozellik

ozellik["isim"] = isim
ozellik["soyisim"] = soyisim
ozellik["ay"] = ay

