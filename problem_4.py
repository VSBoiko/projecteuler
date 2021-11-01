''' Problem 4.

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def num_is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

range_min = 100
range_max = 999
palindromes = []
for x in range(range_max, range_min-1, -1):
    for y in range(range_max, range_min-1, -1):
        if num_is_palindrome(x * y):
            palindromes.append(x * y)

print('answer:', max(palindromes))