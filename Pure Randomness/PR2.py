# Programa que reciba un entero y devuelva True si es numero primo y False si no lo es

primo = True

num = int(input('Num: '))


if num > 1:
    for i in range(2, num):
        if num % i == 0:
            primo = False
elif num < -1:
    for j in range(-2,num,-1):
        if num % j == 0:
                primo = False
else:
    primo = False

print(primo)
