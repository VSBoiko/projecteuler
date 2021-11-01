''' Problem 5.

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20.

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?.'''

num = 0
is_find = False
while not is_find:
    num += 20
    print(num)
    is_find = True
    for i in range(20, 0, -1):
        if num % i != 0:
            is_find = False
            break
   
   
print("answer", num)     