print("""-------------------------------------------------------------------
                    Encode and Decode Message
-------------------------------------------------------------------""")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode_decode(direction, text, shift):
    if direction == "encode":
        encoder = []
        for i in text:
            new_position = int(alphabet.index(i)) + shift
            if new_position > 25:
                new_position -= 26
            encoder += alphabet[new_position]
        print(f"Encoded Message: {''.join(encoder)}")
    elif direction == "decode":
        decoder = []
        for i in text:
            old_position = int(alphabet.index(i)) - shift
            if old_position > 25:
                old_position += 26
            decoder += alphabet[old_position]
        print(f"Decoded Message: {''.join(decoder)}")


encode_decode(direction, text, shift)
print("\n\n\n------------- oulkarshubhu@gmail.com --------------")
