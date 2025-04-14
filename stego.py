'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE IMAGE FILE: drdoes.png
'''

# import modules
from PIL import Image

# the function takes a user a image and hides a hides a secret message in it.
def hide_message():
    image_path = input("Enter the path of the original image: ").strip()
    message = input("Enter the secret message to hide: ").strip()

    #opening the image and converting it to RGB
    img = Image.open(image_path)
    img = img.convert('RGB')

    # converting message to binary format.
    data = []
    for char in message:
        data.extend(format(ord(char), '08b'))

    # iterating through each pixel and embedding the hidden message.
    pixel_index = 0
    for i in range(img.width):
        for j in range(img.height):
            pixel = list(img.getpixel((i, j)))
            for color_channel in range(3):
                if pixel_index < len(data):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + data[pixel_index], 2)
                    pixel_index += 1

            img.putpixel((i, j), tuple(pixel))

    # saving the stego image in a png format.
    stego_image_path = input("Enter the path to save the stego image (e.g., stego_image.png): ").strip()
    img.save(stego_image_path, format='PNG')
    print("Message hidden successfully!")

# run the function.
hide_message()

