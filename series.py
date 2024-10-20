import random

# * Series

# ** Fibonacci

def fibonacci(n=30, a=0, b=1):
    numbers = []
    while len(numbers) < n:
        a, b = b, a + b
        numbers.append(a)
    return numbers

# ** Sieve of Eratosthenes
def primes (n=30):
    numbers = []
    for n in range(2, n):
        for factor in numbers:
            if n % factor == 0:
                break
        else: # no break
            numbers.append(n)
    return numbers


# * Sequences

# ** Binary sequence

def binary_seq (bits=9, shuffle=False):
    seq = list(range(2**bits))
    if shuffle:
        random.shuffle(seq)
    for n in seq:
        yield bin(n)[2:].zfill(bits)
