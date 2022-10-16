"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    for i in range(0,num):
        if(num%i==0)
            return False
    return True

def primes(number_of_primes):
    list = []
    i = 2
    while (len(list)<number_of_primes):
        if(isPrime(i)):
            list[number_of_primes-(number_of_primes-len(list))] = i
        i += 1
    return list
