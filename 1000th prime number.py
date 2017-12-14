# search for the 1000th prime number and print it
# author Zhou Fang  Version: 1.0

# Problem 1.
# Write a program that computes and prints the 1000th prime number.

number_prime = 1
i = 3
while number_prime < 1000:
    divider = 3
    status = 1
    while status:
        if i % divider != 0 and divider < i/2:
            divider = divider +2
        elif divider >= i/2:
            number_prime = number_prime + 1
            prime_num = i
            print('it is the %d th prime number, which is %d' % (number_prime, i))
            status = 0
        else:
            status = 0
    i = i + 2
print('the 1000th prime number is',i-2)
