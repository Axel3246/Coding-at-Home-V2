#https://www.youtube.com/watch?v=IR_S8BC8KI0&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=2&ab_channel=codebasics

def get_squared_numbers (numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers =[2, 5, 8 ,9]
print(get_squared_numbers(numbers))
