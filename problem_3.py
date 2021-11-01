''' Problem 3.

Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''


def is_prime_num(number):
    number_is_prime = True
    for i in range(2, number // 2):
        if number % i == 0:
            number_is_prime = False
            break
        
    return number_is_prime
    
def num_prime_factors(number):
    list_prime_factors = []
    x = 2
    y = number // x
    while x < y:
        if number % x == 0:
            if is_prime_num(x):
                list_prime_factors.append(x)
                
            y = number // x
            if is_prime_num(y):
                list_prime_factors.append(y)
        x += 1
               
    return list_prime_factors

    
prime_factors = num_prime_factors(600851475143)

print('answer:', prime_factors[-1])