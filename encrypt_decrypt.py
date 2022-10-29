alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode_decode(direction, text, shift):
    if direction =="encode":
        message = []
        for i in text:
            message += i
        new_position = 0
        encoder = []
        for i in message:
            new_position = int(alphabet.index(i)) + shift
            encoder += alphabet[new_position]
        print(f"{''.join(encoder)}")
    elif direction == "decode":
        message = []
        for i in text:
            message += i
        old_position = 0
        decoder = []
        for i in message:
            old_position = int(alphabet.index(i)) - shift
            decoder += alphabet[old_position]
        print(f"{''.join(decoder)}")

encode_decode(direction,text,shift)
