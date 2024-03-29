pack = "can,bilgin,230601097,12".lower().split(",")

with open("test.txt", mode="r", encoding="utf-8") as readFile:
    dataPack = readFile.readlines()

print(dataPack)

for i in range(len(dataPack)):
    dataPack[i] = dataPack[i].rstrip()

print(dataPack)