pack = ["a"] 

while True:
    pack = input("Bilgileri sırasıyla girin: ").lower().split(",")
    if len(pack) == 4:
        pack.insert(0, pack.pop(2))
        break
    else:
        print("\nLütfen virgülle ayırarak 4 adet veri girin.")
print(pack)
