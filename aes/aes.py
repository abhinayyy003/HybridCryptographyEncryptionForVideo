from cryptography.fernet import Fernet
import os

# Function to encrypt a video file with AES
def encrypt_video(input_file, encrypted_file, key_file):
    # Read the video file as binary data
    with open(input_file, 'rb') as f:
        video_data = f.read()

    # Generate an AES key
    key = Fernet.generate_key()

    # Create an AES cipher object
    cipher = Fernet(key)

    # Encrypt the video data
    encrypted_video_data = cipher.encrypt(video_data)

    # Save the encrypted video to a new file
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_video_data)

    # Save the AES key securely
    with open(key_file, 'wb') as f:
        f.write(key)

# Function to decrypt a video file using AES
def decrypt_video(encrypted_file, key_file, output_file):
    # Read the encrypted video file as binary data
    with open(encrypted_file, 'rb') as f:
        encrypted_video_data = f.read()

    # Read the AES key from the key file
    with open(key_file, 'rb') as f:
        key = f.read()

    # Create an AES cipher object
    cipher = Fernet(key)

    # Decrypt the video data
    decrypted_video_data = cipher.decrypt(encrypted_video_data)

    # Save the decrypted video to a new file
    with open(output_file, 'wb') as f:
        f.write(decrypted_video_data)
 



# Example usage
if __name__ == '__main__':
    input_video_file = '/Users/abhinay/Desktop/cryptography_PROJECT/aes_input.mp4'  # Replace with your input video file
    encrypted_video_file = 'encrypted_video.mp4'  # Output encrypted video file
    aes_key_file = 'aes_key.key'  # AES key file
    decrypted_video_file = 'decrypted_video.mp4'  # Output decrypted video file

    # Encrypt the video
    encrypt_video(input_video_file, encrypted_video_file, aes_key_file)
    print(f"Video encryption completed. Encrypted video saved to {encrypted_video_file}.")
    print(f"AES key saved to {aes_key_file}. Keep it secure for decryption.")

    # Decrypt the video
    decrypt_video(encrypted_video_file, aes_key_file, decrypted_video_file)
    print(f"Video decryption completed. Decrypted video saved to {decrypted_video_file}.")
