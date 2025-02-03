from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Generate a random 24-byte key for 3DES
key = get_random_bytes(24)

# Initialize the 3DES cipher in ECB mode
cipher = DES3.new(key, DES3.MODE_ECB)

# Encryption
with open('/Users/abhinay/Desktop/cryptography_PROJECT/des_input.mp4', 'rb') as input_file:
    plaintext = input_file.read()

# Padding the plaintext to be a multiple of 8 bytes
plaintext += b'\0' * (8 - len(plaintext) % 8)

ciphertext = cipher.encrypt(plaintext)

with open('encrypted_video.des', 'wb') as output_file:
    output_file.write(ciphertext)

# Decryption
with open('encrypted_video.des', 'rb') as encrypted_file:
    ciphertext = encrypted_file.read()

decrypted_data = cipher.decrypt(ciphertext)

with open('decrypted_video.mp4', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)
