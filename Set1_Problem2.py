# search for the 1000th prime number and print it
# author Zhou Fang  Version: 1.0

# Problem 2.
# Write a program that computes the sum of the logarithms of all the primes from 2 to some number n,
# and print out the sum of the logs of the primes, the number n, and the ratio of these two quantities.
# Test this for different values of n.
from math import *
number_prime = 1
i = 3
n = 5000
sum_prime = log(2)
prime_set = [2]
while number_prime < 1000 and i <= n:
    divider = 3
    status = 1
    while status:
        if i % divider != 0 and divider < i/2:
            divider = divider +2
        elif divider >= i/2:
            number_prime = number_prime + 1
            prime_num = i
            prime_set.append(prime_num)
            print('it is the %d th prime number, which is %d' % (number_prime, i))
            sum_prime = sum_prime + log(prime_set[number_prime - 1])
            print('the sum of log-prime is ', sum_prime)
            status = 0
        else:
            status = 0
    i = i + 2
print('the %d th prime number is %d' % (number_prime, i-2))
print('the sum divided by n is', sum_prime/(i-2))
