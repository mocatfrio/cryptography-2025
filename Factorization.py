from math import sqrt
from math import floor


def get_factors(num):
    # data structure to store the factors
    factors = []
    # the same reasoning as we discussed with primality test
    limit = sqrt(num)+1

    # note: if the given number has small factors: we can find it quite fast (!!!)
    for n in range(2, floor(limit)):
        if num % n == 0:
            factors.append([n, num/n])

    return factors


if __name__ == '__main__':

    # RSA - 2048 bits long integers
    print(get_factors(20))




