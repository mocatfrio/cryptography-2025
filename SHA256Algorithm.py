from hashlib import sha256

# output is a 256 bits long sequence (message digest)
# this is the hash Bitcoin uses
# result is a 64 character long hexadecimal sequence
# 1 hexadecimal character can be stored on 4 bits

s1 = 'Hello world!'
s2 = 'Hello world'

result1 = sha256(s1.encode())
result2 = sha256(s2.encode())

print(result1.hexdigest())
print(result2.hexdigest())



