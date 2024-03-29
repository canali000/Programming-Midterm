digitCheck = input("ID belirle: ")

while True:
    try:
        int(digitCheck)
        if len(digitCheck) == 6:
            break  
        else:
            digitCheck = input("Lütfen 6 haneli bir ID belirle: ")

    except ValueError:
        digitCheck = input("Lütfen ID'yi sayı olarak gir: ")

print(digitCheck)
print(type(digitCheck))

