typeCheckName =  "1"

while True:
    try:
        int(typeCheckName)
    except ValueError:
        break 
    else:
        print("Lütfen ismini harf kullanarak gir.")
        typeCheckName = input("İsim: ")

print(typeCheckName)

