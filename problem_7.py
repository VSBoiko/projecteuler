''' Problem 7.

Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?'''

def is_prime_num(number):
    number_is_prime = True
    for i in range(2, number // 2):
        if number % i == 0:
            number_is_prime = False
            break
        
    return number_is_prime

count = 0
num = 2
primes = []
while count < 10001:
    prime_is_find = False
    while not prime_is_find:
        if is_prime_num(num):
            prime_is_find = True
            count += 1
            last_prime = num
            print(count, num)
            #primes.append(num) 
            
        if (num > 2):
            num += 2
        else:
            num += 1  

        
print('answer:', last_prime)