'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - stego.py
NOTE: USE STEGO IMAGE FILE: drdoes-steg.png
'''

# import modules
from PIL import Image

# prints a header
# prompts a user to enter the path for the stego image.
# opens the image
def extract_message():
    print("Stego Image Extraction Script")
    stego_image_path = input("Enter the path of the stego image: ").strip()
    img = Image.open(stego_image_path)

    # creating a empty string to store data.
    data = ''
    # creating a message terminator that will be used to indicate the end of the message.
    terminator = '11111111'

    # extracing the data from each color channel (RGB) and appends the data bit of each channel to the data string.
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            for color_channel in range(3):
                data += format(pixel[color_channel], '08b')[-1]
    # finding where the message ends
    terminator_index = data.find(terminator)

    # using chr to convert intergers to their corresponding ascii characters.
    message = ''.join([chr(int(data[i:i+8], 2)) for i in range(0, terminator_index, 8)])

    # printing the reconstructed message
    print(f"Extracted Message: {message}")

# main execution block
if __name__ == "__main__":
    extract_message()
