import ascii_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift_number, direction):
    encrypted_message = ""
    decrypted_message = ""
    if direction == "encrypt":
        for char in text:
            if char in alphabet:
                new_index = alphabet.index(char) + shift_number
                encrypted_message += alphabet[new_index]
            else:
                encrypted_message += char
        print(f"Encrypted message: {encrypted_message}")
    elif direction == "decrypt":
        for char in text:
            if char in alphabet:
                original_index = alphabet.index(char) - shift_number
                decrypted_message += alphabet[original_index]
            else:
                decrypted_message += char
        print(f"Decrypted message: {decrypted_message}")

    else:
        print("Invalid input.")


print(ascii_art.logo)

continuing = "yes"
while continuing == "yes":

    choice = input("\nEncrypt or Decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift = int(input("Shift number: "))

    shift = shift % 26

    caesar(message, shift, choice)
    continuing = input("\nWould you like to try again? ")
else:
    print("Goodbye!")
