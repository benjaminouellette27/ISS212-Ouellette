'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - enc-txt.py
NOTE: REMEMBER TO SAVE AES KEY IN **TXT** FILE TO USE FOR DECRYPTION!
'''

# importing modules.
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# function that will take a key size and return a random key in the correct byte size.
def generate_aes_key(key_size):
    return get_random_bytes(key_size // 8)

# creating the AES ciphey in EAX mode
def encrypt_file_aes(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    # reading file content
    with open(file_path, 'rb') as file:
        plaintext = file.read()
        # encrypting content
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    # saving encrypted file
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(cipher.nonce)
        encrypted_file.write(tag)
        encrypted_file.write(ciphertext)

# Example usage
if __name__ == "__main__":
    #generating a 256-bit aes key.
    aes_key = generate_aes_key(256)
    #prompts for file to encrypt
    file_to_encrypt = input("Enter the name of the file to encrypt: ")
    encrypt_file_aes(file_to_encrypt, aes_key)
    print(f'File "{file_to_encrypt}" encrypted.')
    #print aes key.
    print(f'AES Key (Hex): {aes_key.hex()}')