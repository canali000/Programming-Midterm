# SWITCHCASE

car = {
  1: "Ford",
  "2": "Mustang",
  3: "brand"
}

x = car.get(input(),"selamhehe")

print(x)

#############################################################################

## FONKSIYONEL HALE GETIRELIM

# def choice(parametre):
#     car = {
#     1: "Ford",
#     2: "Mustang",
#     3: "BMW"
#     }
#     return car.get(parametre,"HATAAAAAA!!!!")

# while True:
#     x=int(input())
#     print(choice(x))

########################################################################

## SWITCHCASE CALCULATOR

# def sayi():
#     no1= int(input("ilk: "))
#     no2= int(input("second: "))
#     return no1,no2

# def topla():
#     x,y = sayi()
#     return x+y

# def cikar():
#     x,y = sayi()
#     return x-y

# def carp():
#     x,y = sayi()
#     return x*y

# def bol():
#     x,y = sayi()
#     return x//y


# print('''
# 1.ADD
# 2.SUB
# 3.MUL
# 4.DIV
# '''
# )

# choice = int(input("işlem: "))
# operation = [topla,cikar,carp,bol]

# output= operation[choice-1]()

# print(output)


