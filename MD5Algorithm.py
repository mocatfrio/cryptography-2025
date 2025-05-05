# message digest 5 (Rivest back in 1991)
# 128 bits long sequence (hash or the message digest)
# this approach is not collision free !!!
from hashlib import md5

s = 'This is a message!'

result = md5(s.encode())
# 32 hexadecimal characters -
# nibbles (we can store a hexadecimal character on 4 bits - 0.5 byte)
print(result.hexdigest())

