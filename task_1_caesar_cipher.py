def caesar_cipher(text,shift,mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            new_char = chr((ord(ch) - start + shift) % 26 + start)
            result += new_char
        else:
            result += ch
    return result
print("=" * 40),print("      Caesar Cipher Tool"),print("=" * 40)
while True:
    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    choice = input("\nChoose an option (1-3): ")
    if choice == "1":
        message = input("Enter the message: ")
        shift = int(input("Enter shift value: "))
        encrypted = caesar_cipher(message, shift, "encrypt")
        print("\nEncrypted Message:")
        print(encrypted)
    elif choice == "2":
        message = input("Enter the encrypted message: ")
        shift = int(input("Enter shift value used: "))
        decrypted = caesar_cipher(message, shift, "decrypt")
        print("\nDecrypted Message:")
        print(decrypted)
    elif choice == "3":
        print("Program closed.")
        break
    else:
        print("Invalid choice! Please try again.")
