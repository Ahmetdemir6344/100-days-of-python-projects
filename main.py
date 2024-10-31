image=("""
  ____                 _                 
 / ___| ___  ___ _ __| |_ ___ _ __ ___  
| |    / _ \/ _ \ '__| __/ _ \ '_ ` _ \ 
| |___|  __/  __/ |  | ||  __/ | | | | |
 \____|\___|\___|_|   \__\___|_| |_| |_|
""")
print(image)
def caeser(original_text, shift_amount, direction):
    output_text = ''
    if direction == 'decode':
        shift_amount = -shift_amount

    for letter in original_text:
        if letter not in alfabet:
            output_text += letter
        else:
            shifted_position = (alfabet.index(letter) + shift_amount) % len(alfabet)
            output_text += alfabet[shifted_position]

    print(f"Your {direction}d result: {output_text}")


should_continue = True
while should_continue:
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()  # .lower() burada
    shift = int(input("Type the shift number:\n"))

    caeser(text, shift, direction)

    restart = input("Do you want to try again? (yes or no):\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye")















