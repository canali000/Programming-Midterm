def check_ID(search):
    with open("test.txt", mode="r", encoding="utf-8") as readFile:
        check = search
        for id in readFile:
            id = id.rstrip()
            if id == check:
                return True
        return False
    
search = input("ID: ")
while check_ID(search) == True:
    print("Bu ID kullanılmış.")
    search = input("Lüfen yeni bir ID belirleyin: ")
    check_ID(search)

print(search)