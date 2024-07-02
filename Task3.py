from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Apply a basic mathematical operation to each pixel value
    encrypted_pixels = (pixels + key) % 256
    
    # Convert array back to image
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)
    
    # Reverse the mathematical operation
    decrypted_pixels = (pixels - key) % 256
    
    # Convert array back to image
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    input_path = input("Enter the input image file path: ")
    output_path = input("Enter the output image file path: ")
    key = int(input("Enter the key (integer value): "))
    
    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
