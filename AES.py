from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

# private key of the AES (used for encryption and for decryption)
# 128 bits (16 bytes)
# key = get_random_bytes(16)

# you may ask for a password from the user and then
# you can use the first 16 bytes
# ask for a password - and then use a SHA (hashing) 16 bytes
key = b'mysecretpassword'

cipher = AES.new(key, AES.MODE_CBC)

plaintext = b'This is a message!'

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
iv = cipher.iv

decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
original_text = unpad(decrypt_cipher.decrypt(ciphertext), AES.block_size)

print(original_text.decode())

