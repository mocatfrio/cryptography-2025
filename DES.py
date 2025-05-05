from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

key = b'mysecret'
key2 = get_random_bytes(8)
print(key2)

cipher = DES.new(key, DES.MODE_CBC)
print(cipher.iv)
print(DES.block_size)

plain = b'This is my message'
print(pad(plain, DES.block_size))

ciphertext = cipher.encrypt(pad(plain, DES.block_size))
iv = cipher.iv

decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
original_test = unpad(decrypt_cipher.decrypt(ciphertext), DES.block_size)

print(original_test.decode())
