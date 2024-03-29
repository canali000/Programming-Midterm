with open('test.txt', 'r') as dosya:
    for satir in dosya:
        print(satir.rstrip())
    # Döngü dosyanın sonuna geldiğinde bu noktaya ulaşılır
    print("Dosyanın sonuna geldim.")
