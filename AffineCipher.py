import string

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist")

def remove_punctuation(text):
    """Remove punctuation and non-alphabetic characters from text."""
    return ''.join(char for char in text if char.isalpha())

def affine_encrypt(plaintext, a, b):
    """Encrypt plaintext using the Affine cipher."""
    plaintext = remove_punctuation(plaintext)  # Remove punctuation
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26")
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            num = ord(char) - ord('A')
            encrypted_num = (a * num + b) % 26
            ciphertext += chr(encrypted_num + ord('A'))
        else:
            ciphertext += char  # Keep non-alphabetic characters unchanged
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """Decrypt ciphertext using the Affine cipher."""
    ciphertext = remove_punctuation(ciphertext)  # Remove punctuation
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26")
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    for char in ciphertext.upper():
        if char.isalpha():
            num = ord(char) - ord('A')
            decrypted_num = (a_inv * (num - b)) % 26
            plaintext += chr(decrypted_num + ord('A'))
        else:
            plaintext += char  # Keep non-alphabetic characters unchanged
    return plaintext

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__":
    a = 5  # Multiplicative key
    b = 8  # Additive key
    plaintext = "Cryptography is essential for protecting information in computing systems and plays a significant role in the daily lives of billions of people worldwide by securing both stored and transmitted data. As a fundamental element of many security protocols, particularly Transport Layer Security (TLS), cryptographic techniques enable strong encryption across various applications. However, despite its importance, cryptography remains susceptible to vulnerabilities—its security can be entirely compromised by a single design flaw or programming error. Traditional software testing methods, such as unit testing, are insufficient for detecting cryptographic weaknesses. Instead, cryptographic security is established through rigorous mathematical proofs and formal analysis to ensure compliance with critical security principles, often based on reasonable assumptions. One of the early encryption methods that evolved beyond simple substitution ciphers is the Affine cipher, which applies a linear transformation to each letter using modular arithmetic. Unlike basic monoalphabetic ciphers, the Affine cipher introduces additional complexity by incorporating both multiplication and addition in the encryption process. However, despite its improved structure, it remains vulnerable to cryptanalysis techniques such as frequency analysis and known-plaintext attacks, which can reveal the encryption key. This underscores a key principle in modern cryptography: true security depends not only on secrecy but also on strong mathematical foundations and computational infeasibility."
    ciphertext = affine_encrypt(plaintext, a, b)
    print("Ciphertext:", ciphertext)

    decrypted_text = affine_decrypt(ciphertext, a, b)
    print("Decrypted text:", decrypted_text)
