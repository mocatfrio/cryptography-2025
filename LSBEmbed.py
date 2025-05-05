from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    pixels = encoded.load()

    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # End marker
    message_index = 0

    for y in range(height):
        for x in range(width):
            if message_index < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[message_index])
                message_index += 1
                if message_index < len(binary_message):
                    g = (g & ~1) | int(binary_message[message_index])
                    message_index += 1
                if message_index < len(binary_message):
                    b = (b & ~1) | int(binary_message[message_index])
                    message_index += 1
                pixels[x, y] = (r, g, b)
            else:
                break

    # Verify that the embedding process correctly embeds the message and includes the end marker
    extracted_binary = ''
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            extracted_binary += str(r & 1)
            extracted_binary += str(g & 1)
            extracted_binary += str(b & 1)
            if len(extracted_binary) >= len(binary_message):
                break
        if len(extracted_binary) >= len(binary_message):
            break

    if extracted_binary[:len(binary_message)] == binary_message:
        print("Verification successful: Message embedded correctly.")
    else:
        print("Verification failed: Embedded message does not match.")

    encoded.save(output_path)
    print(f"Message encoded and saved to {output_path}")

# Example usage
# encode_message('input_image.png', 'Your secret message', 'output_image.png')
if __name__ == "__main__":
    plainteks = "Cryptography is essential for protecting information in computing systems and plays a significant role in the daily lives of billions of people worldwide by securing both stored and transmitted data. As a fundamental element of many security protocols, particularly Transport Layer Security (TLS), cryptographic techniques enable strong encryption across various applications. However, despite its importance, cryptography remains susceptible to vulnerabilities—its security can be entirely compromised by a single design flaw or programming error. Traditional software testing methods, such as unit testing, are insufficient for detecting cryptographic weaknesses. Instead, cryptographic security is established through rigorous mathematical proofs and formal analysis to ensure compliance with critical security principles, often based on reasonable assumptions. One of the early encryption methods that evolved beyond simple substitution ciphers is the Affine cipher, which applies a linear transformation to each letter using modular arithmetic. Unlike basic monoalphabetic ciphers, the Affine cipher introduces additional complexity by incorporating both multiplication and addition in the encryption process. However, despite its improved structure, it remains vulnerable to cryptanalysis techniques such as frequency analysis and known-plaintext attacks, which can reveal the encryption key. This underscores a key principle in modern cryptography: true security depends not only on secrecy but also on strong mathematical foundations and computational infeasibility."
    encode_message("./bromo.jpeg", plainteks, "./bromo_embed.jpeg")

