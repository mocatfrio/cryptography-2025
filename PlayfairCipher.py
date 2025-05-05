import string

def generate_key_matrix(key):
    """Generate a 5x5 key matrix for the Playfair Cipher."""
    key = ''.join(dict.fromkeys(key.replace('J', 'I')))  # Remove duplicates, replace J with I
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_matrix = [char for char in key if char in alphabet]
    key_matrix += [char for char in alphabet if char not in key_matrix]
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def preprocess_text(text):
    """Preprocess text for Playfair Cipher."""
    text = ''.join(filter(str.isalpha, text.upper())).replace('J', 'I')  # Remove non-alphabetic characters
    processed = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed.append(text[i] + 'X')
            i += 1
        elif i + 1 < len(text):
            processed.append(text[i] + text[i + 1])
            i += 2
        else:
            processed.append(text[i] + 'X')
            i += 1
    return processed

def find_position(char, key_matrix):
    """Find the row and column of a character in the key matrix."""
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(pair, key_matrix):
    """Encrypt a pair of characters using the Playfair Cipher."""
    row1, col1 = find_position(pair[0], key_matrix)
    row2, col2 = find_position(pair[1], key_matrix)
    if row1 == row2:  # Same row
        return key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle
        return key_matrix[row1][col2] + key_matrix[row2][col1]

def decrypt_pair(pair, key_matrix):
    """Decrypt a pair of characters using the Playfair Cipher."""
    row1, col1 = find_position(pair[0], key_matrix)
    row2, col2 = find_position(pair[1], key_matrix)
    if row1 == row2:  # Same row
        return key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle
        return key_matrix[row1][col2] + key_matrix[row2][col1]

def encrypt(text, key):
    """Encrypt text using the Playfair Cipher."""
    key_matrix = generate_key_matrix(key)
    pairs = preprocess_text(text)
    print(pairs)
    return ''.join(encrypt_pair(pair, key_matrix) for pair in pairs)

def decrypt(ciphertext, key):
    """Decrypt ciphertext using the Playfair Cipher."""
    key_matrix = generate_key_matrix(key)
    pairs = preprocess_text(ciphertext)
    return ''.join(decrypt_pair(pair, key_matrix) for pair in pairs)

# Example usage
if __name__ == "__main__":
    key = "SRIGALACANTIK"
    plaintext = "Cryptography is essential for protecting information in computing systems and plays a vital role in the daily lives of billions of people worldwide by securing both stored and transmitted data. Fundamental to many security protocols, particularly Transport Layer Security (TLS), cryptographic techniques enable robust encryption across various applications. However, despite its importance, cryptography remains fragile—its security can be completely undermined by a single design flaw or programming error. Traditional software testing methods, such as unit testing, are insufficient for detecting cryptographic vulnerabilities. Instead, cryptographic security is established through rigorous mathematical proofs and formal analysis to ensure compliance with essential security principles, often relying on reasonable assumptions. One of the early encryption methods that improved upon simple substitution ciphers is the Playfair cipher, introduced in the 19th century. Unlike monoalphabetic ciphers, Playfair encrypts pairs of letters using a 5x5 key square, making frequency analysis more difficult. While it was once considered a significant advancement, modern cryptanalysis techniques can break Playfair encryption by exploiting digram frequency distributions and reconstructing the key square. This underscores a fundamental concept in contemporary cryptography: true security depends not only on secrecy but also on strong mathematical principles and computational infeasibility."
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
