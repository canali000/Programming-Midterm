typeCheckID =  "a"

while True:
    try:
        typeCheckID = int(typeCheckID)
        break

    except ValueError:
        typeCheckID = input("Lütfen ID gir: ")


print(typeCheckID)

