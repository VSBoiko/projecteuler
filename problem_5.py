''' Problem 5.

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20.

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?.'''


def divided_by_each(div_from = 1, div_to = 10):
    num = 0
    list_divided = range(div_from, div_to+1)
    is_find = False
    while not is_find:
        num += list_divided[-1] * list_divided[-2]
        is_find = True
        for i in list_divided[::-1]:
            if num % i != 0:
                is_find = False
                break
    return num

   
   
print("answer", divided_by_each(1, 20))

# 232792560