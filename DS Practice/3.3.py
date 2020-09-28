#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
#https://github.com/codebasics/py/blob/master/DataStructures/2_Arrays/2_arrays_exercise.md

largo = int(input("Número Máximo: "))

odd_n=[]

for i in range(largo):
    if i%2 == 1:
        odd_n.append(i)

print(odd_n)

