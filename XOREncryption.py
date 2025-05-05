import sys

def xor_encrypt_decrypt(input_data, key):
    """Encrypt or decrypt input data using XOR with the given key."""
    output_data = bytearray()
    key_length = len(key)
    
    for i in range(len(input_data)):
        output_data.append(input_data[i] ^ key[i % key_length])
    
    return output_data

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python3 XOREncryption.py <encrypt|decrypt> <input_file> <output_file> <key>")
        sys.exit(1)

    command = sys.argv[1].lower()
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    key = sys.argv[4]

    if command not in ["encrypt", "decrypt"]:
        print("Error: Command must be 'encrypt' or 'decrypt'.")
        sys.exit(1)

    try:
        # Read input file
        with open(input_file, "rb" if command == "decrypt" else "r", encoding=None if command == "decrypt" else "utf-8") as file:
            input_data = file.read()

        # Convert input data and key to bytearray
        input_bytes = bytearray(input_data) if command == "decrypt" else bytearray(input_data, 'utf-8')
        key_bytes = bytearray(key, 'utf-8')

        # Encrypt or decrypt the input data
        result_data = xor_encrypt_decrypt(input_bytes, key_bytes)

        # Write the result to the output file
        with open(output_file, "wb" if command == "encrypt" else "w", encoding=None if command == "encrypt" else "utf-8") as file:
            file.write(result_data if command == "encrypt" else result_data.decode('utf-8'))

        print(f"{command.capitalize()}ion completed. Output written to {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
