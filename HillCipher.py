import numpy as np
import string

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist")

def matrix_mod_inverse(matrix, modulus):
    """Find the modular inverse of a matrix under a given modulus."""
    det = int(round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_mod = det % modulus
    det_inv = mod_inverse(det_mod, modulus)  # Modular inverse of the determinant

    # Adjugate matrix
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus

def text_to_numbers(text):
    """Convert text to a list of numbers (A=0, B=1, ..., Z=25)."""
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def numbers_to_text(numbers):
    """Convert a list of numbers to text (0=A, 1=B, ..., 25=Z)."""
    return ''.join(chr(num + ord('A')) for num in numbers)

def remove_punctuation(text):
    """Remove punctuation and non-alphabetic characters from text."""
    return ''.join(char for char in text if char.isalpha())

def hill_encrypt(plaintext, key_matrix):
    """Encrypt plaintext using the Hill cipher."""
    plaintext = remove_punctuation(plaintext)  # Remove punctuation
    plaintext_numbers = text_to_numbers(plaintext)
    n = key_matrix.shape[0]
    # Pad plaintext to make its length a multiple of the key matrix size
    while len(plaintext_numbers) % n != 0:
        plaintext_numbers.append(0)  # Padding with 'A' (0)

    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, n)
    ciphertext_matrix = (np.dot(plaintext_matrix, key_matrix) % 26).astype(int)
    ciphertext_numbers = ciphertext_matrix.flatten()
    return numbers_to_text(ciphertext_numbers)

def hill_decrypt(ciphertext, key_matrix):
    """Decrypt ciphertext using the Hill cipher."""
    ciphertext = remove_punctuation(ciphertext)  # Remove punctuation
    ciphertext_numbers = text_to_numbers(ciphertext)
    n = key_matrix.shape[0]
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, n)
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    plaintext_matrix = (np.dot(ciphertext_matrix, key_matrix_inv) % 26).astype(int)
    plaintext_numbers = plaintext_matrix.flatten()
    return numbers_to_text(plaintext_numbers)

# Example usage
if __name__ == "__main__":
    key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix
    plaintext = "Hello Cyber Fox, attacker here! Cryptography is crucial for safeguarding information in computing systems and plays an integral role in the daily lives of billions of people worldwide by ensuring the security of both stored and transmitted data. As a core component of many security protocols, particularly Transport Layer Security (TLS), cryptographic methods provide strong encryption across various applications. However, despite its significance, cryptography remains vulnerable—its security can be entirely compromised by a single design flaw or coding error. Traditional software testing techniques, such as unit testing, are inadequate for identifying cryptographic weaknesses. Instead, cryptographic security is reinforced through rigorous mathematical proofs and formal analysis to verify adherence to critical security principles, often based on reasonable assumptions. One of the early encryption techniques that advanced beyond simple substitution ciphers is the Hill cipher, developed in the 20th century. Unlike monoalphabetic ciphers, the Hill cipher uses linear algebra and matrix multiplication to encrypt blocks of letters simultaneously, making it more resistant to frequency analysis. However, despite its mathematical sophistication, it can be decrypted if an attacker obtains enough plaintext-ciphertext pairs, allowing them to solve for the encryption matrix. This highlights a fundamental principle in modern cryptography: true security relies not just on secrecy but also on solid mathematical foundations and computational infeasibility."
    ciphertext = hill_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = hill_decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
