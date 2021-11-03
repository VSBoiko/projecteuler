''' Problem 6.

Сумма квадратов первых десяти натуральных чисел равна
1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет
3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def sum_sqr(count_numbers=10):
    result = 0
    for i in range(1, count_numbers+1):
        result += i**2
    
    return result

def sqr_sum(count_numbers=10):
    summ = 0
    for i in range(1, count_numbers+1):
        summ += i
    result = summ**2
    return result
        
print('answer:', sqr_sum(100) - sum_sqr(100))