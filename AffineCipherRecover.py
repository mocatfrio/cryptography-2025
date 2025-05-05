import math

def modular_inverse(a, n):
    for i in range(n):
        if (a * i) % n == 1:
            return i
    return None

def affine_decipher(hex_values, m, b, n):
    m_inverse = modular_inverse(m, n)
    if m_inverse is None:
        raise ValueError("Multiplicative inverse of m does not exist.")

    plain_hex = []
    for i in range(len(hex_values)):
        P = hex((m_inverse * (int(hex_values[i], 16) - b)) % n)
        plain_hex.append(P)
    return plain_hex


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


def array_of_hex_to_bytearray(array_of_hex):
    bytearray_data = bytearray()
    for hex_value in array_of_hex:
        if hex_value.startswith("0x"):
            hex_value = hex_value[2:]
        byte_value = int(hex_value, 16)
        bytearray_data.append(byte_value)
    return bytearray_data


def create_file_from_bytes(file_path, bytes_data):
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_data)
            print("File berhasil dibuat:", file_path)
    except Exception as e:
        print("Error:", e)


def main(image_path, m, b):
    n = 256
    hex_values = read_image_to_hex(image_path)
    if hex_values is not None:
        plain_hex = affine_decipher(hex_values, m, b, n)
        bytearray_plain = array_of_hex_to_bytearray(plain_hex)
        create_file_from_bytes(
            image_path.split(".")[0] + "_recovered." + image_path.split(".")[1],
            bytearray_plain,
        )

if __name__ == "__main__":
    image_path = "affinecipher.jpeg"
    m = 115  # Replace with the actual value of m used during encryption
    b = 42   # Replace with the actual value of b used during encryption
    main(image_path, m, b)
