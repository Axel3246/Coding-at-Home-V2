#https://www.youtube.com/watch?v=daefaLgNkw0&ab_channel=CoreySchafer
Estudiante = {'nombre': 'Jhon','edad': 25, 'cursos':['Matemáticas', 'Computación']} #Empieza el dict

#o

Estudiante1 = dict(Nombre ='Jhon', Edad = 25) #También se puede de esta forma


Estudiante['telefono'] = '555-555-555' #Agrega una llave con un valor al diccionario

Estudiante.update({'nombre':'Axel', 'edad': 18}) #Modifica el diccionario con el .update()
del Estudiante['edad'] #Elimina una llave del diccionario

print(Estudiante) #Imprime el dict
print(Estudiante1)
print(Estudiante.get('nombre')) #Imprime solo el nombre o cualquier otra variable en el dict
print(Estudiante.get('telefono', 'No se encontró')) #Si no existe la llave, retorna el mensaje que no lo encontró

print(len(Estudiante)) #Da el largo del dict
print(Estudiante.keys()) #Devuelve todas las llaves
print(Estudiante.values()) #Devuelve todos los valores
print(Estudiante.items()) #Devuelve ambas cosas
 
#iteration

for i in Estudiante.items():   #o .values, o.keys, o simplemente Estudiante
    print(i)