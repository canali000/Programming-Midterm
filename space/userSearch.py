with open("test.txt", mode="r", encoding="utf-8") as readFile:
    while True:
        dataPack = []
        search = "230601097"
        id = readFile.readline().rstrip()
        if id == search:
            dataPack.append(id)    
            for i in range(0,4):
                data = readFile.readline().rstrip()
                dataPack.append(data)    
            break

print(dataPack)