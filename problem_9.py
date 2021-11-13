''' Problem 9.

Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def if_pythagorean_triple(a: int, b: int, c: int) -> bool:
    result = False
    if a ** 2 + b ** 2 == c ** 2:
        result = True

    return result

answer = {}
for a in range(1, 1000):
    for b in range(a+1, 1000-a+1):
        c = 1000 - a - b
        if if_pythagorean_triple(a, b, c):
            answer = {
                'multiply': a * b * c,
                'sequence': f'{a} {b} {c}'
            }

print('answer:', answer)
