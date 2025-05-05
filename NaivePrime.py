from math import sqrt
from math import floor


def is_prime(num):

    if num < 2:
        return False

    # is the only even prime number
    if num == 2:
        return True

    # even numbers can not be primes
    if num % 2 == 0:
        return False

    # we have already checked numbers < 3
    # finding primes up to N we just have to check numbers up to sqrt(N)
    # increment by 2 because we have already considered even numbers
    for n in range(3, floor(sqrt(num))+1, 2):
        if num % n == 0:
            return False

    return True


if __name__ == '__main__':

    print(is_prime(99194853094755497))