'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - de-txt.py
NOTE: USE AES KEY IN **TXT** FILE TO DECRYPT FILE: sup3rs3cr37.txt.enc
'''

#import modules
from Crypto.Cipher import AES

# Function decrypts a file using a user provided key.
# opens the file in a read binary mode
# reads the first 16 bytes as the nonce
# reads the next 16 as the tag
# reads the rest as the ciphertext.
def decrypt_file_aes(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        nonce = encrypted_file.read(16)
        tag = encrypted_file.read(16)
        ciphertext = encrypted_file.read()

    # decrypting the cipher text.
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    #saving decrypted file to a new file.
    #adds the _decrypted.txt ending to the decrypted file.
    with open(encrypted_file_path[:-4] + '_decrypted.txt', 'wb') as decrypted_file:
        decrypted_file.write(plaintext)


# Execution the main block.
if __name__ == "__main__":
    # user prompt to get AES key
    aes_key = bytes.fromhex(input("Enter the AES key (hexadecimal format): "))
    # getting the file path
    file_to_decrypt = input("Enter the name of the file to decrypt: ")
    #calling the decrypt function
    decrypt_file_aes(file_to_decrypt, aes_key)
    #output
    print(f'File "{file_to_decrypt}" decrypted.')
