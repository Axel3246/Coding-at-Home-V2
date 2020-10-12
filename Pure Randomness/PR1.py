'''
Programa que cuenta la edad, si es local o foraneo
'''

clientes = int(input("Escribe el numero de clientes: "))
Total = 0
conteoPersonas = 1
pMayores = 0
foraneos = 0
locales = 0

while conteoPersonas <= clientes:
    edad = int(input("Escribe tu edad: "))
    ciudad = input("Escribe tu ciudad: ")
    if edad >= 18:
        if ciudad == "Monterrey":
            pMayores += 1
            locales += 1
        elif ciudad != "Monterrey":
            foraneos += 1
            pMayores += 1
    if edad < 18:
        if ciudad == "Monterrey":
            locales += 1
        if ciudad != "Monterrey":
            foraneos += 1
    
    conteoPersonas += 1

print("Numeros de personas mayores :" + str(pMayores))
print(locales, foraneos)