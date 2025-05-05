

# in our implementation a<b
def egcd(a, b):

    # base-case
    # of course because gcd(0,b)=b and a*x+b*y=b - so x=0 and y=1
    if a == 0:
        return b, 0, 1

    # so we use the Euclidean algorithm for gcd()
    # b%a is always the smaller number - and 'a' is the smaller integer
    # always in this implementation
    gcd, x1, y1 = egcd(b % a, a)

    # and we update the parameters for x, y accordingly
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


if __name__ == '__main__':
    print(egcd(7, 9))

