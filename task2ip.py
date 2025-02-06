import cv2
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Simple image encryption using XOR operation
    """
    # Read the image
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError("Could not read the image")
    
    # Convert key to uint8
    key = np.uint8(key)
    
    # Create a key array of the same size as the image
    key_array = np.full_like(img, key)
    
    # Perform XOR encryption
    encrypted_img = cv2.bitwise_xor(img, key_array)
    
    # Save the encrypted image
    cv2.imwrite(output_path, encrypted_img)
    return True

def decrypt_image(input_path, output_path, key):
    """
    Decrypt the image using the same XOR operation
    """
    # Read the encrypted image
    encrypted_img = cv2.imread(input_path)
    if encrypted_img is None:
        raise ValueError("Could not read the encrypted image")
    
    # Convert key to uint8
    key = np.uint8(key)
    
    # Create a key array of the same size as the image
    key_array = np.full_like(encrypted_img, key)
    
    # Perform XOR decryption (same operation as encryption)
    decrypted_img = cv2.bitwise_xor(encrypted_img, key_array)
    
    # Save the decrypted image
    cv2.imwrite(output_path, decrypted_img)
    return True

# Example usage
if __name__ == "__main__":
    # Set your encryption key (0-255)
    key = 123
    
    try:
        # Encrypt
        print("Encrypting image...")
        encrypt_image("input.jpg", "encrypted.jpg", key)
        print("Image encrypted successfully!")
        
        # Decrypt
        print("Decrypting image...")
        decrypt_image("encrypted.jpg", "decrypted.jpg", key)
        print("Image decrypted successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")