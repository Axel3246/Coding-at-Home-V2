#Excercise from 3: https://github.com/codebasics/py/blob/master/DataStructures/2_Arrays/2_arrays_exercise.md

Expenses = [2200, 2350, 2600, 2130, 2190]

#1. In Feb, how many dollars you spent extra compare to January?

print("Compared to January, February I spent " + str(Expenses[1]-Expenses[0]) + " more.")

#2. Find out your total expense in first quarter (first three months) of the year.

print(Expenses[0]+Expenses[1]+Expenses[2])

#3. Find out if you spent exactly 2000 dollars in any month

for i in range(len(Expenses)):
        if Expenses[i] == 2000:
            print("Si hay gastos de 2000")
            break
        else:
            print("No hay gastos de 2000")
            break

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

#Otra Respuesta : Expenses.append(1980)

Expenses.insert(5,1980)

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list

#Otra Respuesta : Expenses[3] = Expenses[3] - 200

Expenses.remove(2130)
Expenses.insert(3,1930)
print(Expenses)




