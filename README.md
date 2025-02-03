# Hybrid Cryptography Encryption For Video

Hybrid Cryptography Encryption Video is an encryption Technique that combines **AES** and **3DES** to securely encrypt video files. The video is split into two halves, where:  
- One half is encrypted using **AES**  
- The other half is encrypted using **3DES (Triple DES)**  
- Both encrypted halves are stored separately  
- During decryption, the original video is reconstructed  


## How It Works

1. **Video Splitting** – The input_video.mp4 is divided into two parts.  
2. **AES Encryption** – The first half is encrypted using AES.  
3. **3DES Encryption** – The second half is encrypted using 3DES.  
4. **Storage** – The encrypted halves are stored separately.  
5. **Decryption** – Both halves are decrypted using AES and 3DES.  
6. **Merging** – The decrypted halves are combined to reconstruct the original video.  

## How To Run
```sh main.sh```

note: make sure that the input video is named as `input_video.mp4`
