def caesar_cipher(text, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift
        
    for char in text:
        if char.isalpha():
            new_pos = (ord(char.lower()) - ord('a') + shift) % 26
            result += chr(new_pos + ord('a'))
        else:
            result += char
            
    return result

while True:
    print("\nSimple Caesar Cipher")
    print("Type 'quit' to exit")
    
    text = input("\nEnter message: ")
    if text.lower() == 'quit':
        break
        
    shift = int(input("Enter shift (1-25): "))
    mode = input("Encrypt or decrypt? (e/d): ")
    
    if mode.lower() == 'e':
        result = caesar_cipher(text, shift)
        print("Encrypted:", result)
    else:
        result = caesar_cipher(text, shift, False)
        print("Decrypted:", result)