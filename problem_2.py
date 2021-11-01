''' Problem 2.

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''


def fibonacci(max=10):
    list_fibonacci = [1, 2]
    while list_fibonacci[-1] <= max:
        new = sum(list_fibonacci[-2:])
        list_fibonacci.append(new)
    else:
        del(list_fibonacci[-1])
        
    return list_fibonacci

    
fib = fibonacci(4000000)
sum = 0
for i in fib:
    if i % 2 == 0:
        sum += i

print('answer:', sum)