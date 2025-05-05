from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    binary_message = ''
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Split binary message into 8-bit chunks and convert to characters
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''
    for char in chars:
        if char == '11111110':  # End marker
            break
        message += chr(int(char, 2))

    print("Decoded message:", message)
    return message

# Example usage
# decode_message('output_image.png')
if __name__ == "__main__":
    decode_message("./bromo_embed.jpeg")
