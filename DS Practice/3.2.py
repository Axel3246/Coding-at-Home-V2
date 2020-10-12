#Excercise from 3: https://github.com/codebasics/py/blob/master/DataStructures/2_Arrays/2_arrays_exercise.md

heros=['spider man','thor','hulk','iron man','captain america']

#1. Length of the list

print(len(heros))

#2. Add 'black panther' at the end of this list

heros.append("black panther")
print(heros)

#3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

#4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

#Otra respuesta : heros.remove[1:3] = ["doctor strange"]

heros.remove("hulk"), heros.remove("thor"), heros.insert(1,"doctor strange")
print(heros)

#5. 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)

#In or not in to determine whether a string or int is in a list/attay
# n = int(input())
#list[]
# for i in range n:
#   list.append(str(input()))
#print(lista)