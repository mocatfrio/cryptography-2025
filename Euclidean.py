

# recursive implementation
def gcd(a, b):

    # base-case: if b|a (without a remainder) then b is the gcd
    if a % b == 0:
        return b

    # keep calling the function recursively
    return gcd(b, a % b)


def gcd_iter(a, b):
    # we make iterations until b|a without a remainder
    while a % b != 0:
        a, b = b, a % b

    # if b|a then b is the greatest common divisor
    return b


if __name__ == '__main__':
    print(gcd_iter(24, 9))