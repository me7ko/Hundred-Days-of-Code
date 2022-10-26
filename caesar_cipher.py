alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {cipher_direction}d text is {end_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'end' to quit the program:\n")
    if direction == "end":
        quit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)