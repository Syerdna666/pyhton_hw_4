# Задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# 60 -> 2, 2, 3, 5

def factorization(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result

print(factorization(60))


# Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе.
#  Выведите названия того товара, который закончился.

# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»


def openFile(nameFile):
    data = open(nameFile, encoding='utf-8')
    item = data.readlines()
    data.close()
    list = item[0].split(', ')
    return set(list)

stock = openFile('stock_iceCream.txt')
out_of_stock = openFile('out_of_stock_iceCream.txt')
print(f"Закончилось: {' '.join(stock.difference(out_of_stock))}")


# Задача 3. Выведите число π с заданной точностью. 
# Точность вводится пользователем в виде натурального числа. 

# 3 -> 3.142
# 5 -> 3.14159

import math

def accuracy_of_pi():
    N = int(input("Enter accuracy of pi: "))
    res = round(math.pi, N)
    return res

print(accuracy_of_pi())



