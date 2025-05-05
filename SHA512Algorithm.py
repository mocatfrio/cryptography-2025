from hashlib import sha512

# output is a 512 bits long sequence (message digest)
# this is the hash Bitcoin uses
# result is a 128 character long hexadecimal sequence
# 1 hexadecimal character can be stored on 4 bits
# 2^512 = the number of possible hashes
# because of the birthday paradox - 2^256

s1 = 'Hello world!'
s2 = 'Hello world'

result1 = sha512(s1.encode())
result2 = sha512(s2.encode())

print(result1.hexdigest())
print(result2.hexdigest())



