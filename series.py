import random
from collections.abc import Iterator

# * Series

# ** Fibonacci

# Fibonacci numbers: https://oeis.org/A000045


def fibonacci(limit: int = 30, a: int = 0, b: int = 1) -> list[int]:
    """Return the Fibonacci numbers until limit."""
    numbers = [a] if a > 0 else []
    while len(numbers) < limit:
        a, b = b, a + b
        numbers.append(a)
    return numbers


# ** Lucas

# Lucas numbers: https://oeis.org/A000032


def lucas(limit: int = 30) -> list[int]:
    """Return the Lucas numbers until limit."""
    return fibonacci(limit, 2, 1)


# ** Sieve of Eratosthenes


def primes(limit: int = 30) -> list[int]:
    """Return the list of the first prime numbers until limit."""
    numbers = []
    for n in range(2, limit):
        for factor in numbers:
            if n % factor == 0:
                break
        else:  # no break
            numbers.append(n)
    return numbers


# * Sequences

# ** Binary sequence


def binary_seq(bits: int = 9, shuffle: bool = False) -> Iterator[str]:
    """Return zero-padded binary strings for the number of bits.

    If shuffle is True, shuffle the sequence.

    Yields:
        str: A zero-padded binary string.

    """
    seq = list(range(2**bits))
    if shuffle:
        random.shuffle(seq)
    for n in seq:
        yield bin(n)[2:].zfill(bits)
