import math

def modular_inverse(a, n):
    for i in range(n):
        if (a * i) % n == 1:
            return i
    return None

def calculate_keys(P1, C1, P2, C2, n):
    delta_P = (P2 - P1) % n
    delta_C = (C2 - C1) % n

    m_inverse = modular_inverse(delta_P, n)
    if m_inverse is None:
        raise ValueError("Modular inverse does not exist for delta_P.")

    m = (delta_C * m_inverse) % n
    b = (C1 - m * P1) % n

    return m, b

def read_image_to_hex(image_path):
    try:
        with open(image_path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            array_of_hex = [hex(byte) for byte in b]
            return array_of_hex
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except ValueError as e:
        print("Error:", e)
        return None

def hex_to_int(hex_value):
    """Convert a hexadecimal string (e.g., '0x1a') to an integer."""
    return int(hex_value, 16)

def calculate_keys_from_hex(P1_hex, C1_hex, P2_hex, C2_hex, n):
    """Calculate m and b using pairs in hexadecimal format."""
    P1 = hex_to_int(P1_hex)
    C1 = hex_to_int(C1_hex)
    P2 = hex_to_int(P2_hex)
    C2 = hex_to_int(C2_hex)

    return calculate_keys(P1, C1, P2, C2, n)

# Example usage
if __name__ == "__main__":
    plainteks = read_image_to_hex("bromo.jpeg")
    cipherteks = read_image_to_hex("affinecipher.jpeg")

    # Replace these values with actual plaintext and ciphertext pairs in hex
    P1_hex, C1_hex = plainteks[0], cipherteks[0]  # Example pair 1
    P2_hex, C2_hex = plainteks[1], cipherteks[1]  # Example pair 2
    print(P1_hex, C1_hex, P2_hex, C2_hex)
    n = 256  # Modulus for byte values

    try:
        m, b = calculate_keys_from_hex(P1_hex, C1_hex, P2_hex, C2_hex, n)
        print(f"Calculated keys: m={m}, b={b}")
    except ValueError as e:
        print("Error:", e)
