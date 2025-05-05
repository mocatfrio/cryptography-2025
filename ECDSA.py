from Crypto.Hash import SHA256
# ECC elliptic curve cryptography
from Crypto.PublicKey import ECC
# DSS digital signature standard
from Crypto.Signature import DSS

key = ECC.generate(curve='P-256')

# print(key)
# print(key.public_key())

message = "Transaction #322121 is sent from A to B in Bitcoin"
# we convert any messages to 256 bits long hash
message_hash = SHA256.new(message.encode())

signer = DSS.new(key, "fips-186-3")
signature = signer.sign(message_hash)

print(signature)

### verify the signature
verifier = DSS.new(key, "fips-186-3")

try:
    verifier.verify(message_hash, signature)
    print("The signature is valid...")
except ValueError:
    print("The signature is invalid...")

















