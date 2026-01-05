import random
import string

def get_random_chars(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))

def encode(word):
    if len(word) < 1:
        return ""
    first_letter = word[0]
    remaining = word[1:] + first_letter
    prefix = get_random_chars()
    suffix = get_random_chars()
    coded = prefix + remaining + suffix
    return coded

def decode(word):
    if len(word) < 7:
        return ""
    core = word[3:-3]
    last_letter = core[-1]
    decoded = last_letter + core[:-1]
    return decoded

def main():
    user_input = input("Enter 'e' to encode or 'd' to decode: ").lower()
    if user_input == 'e':
        word = input("Enter word to encode: ")
        encoded_word = encode(word)
        print("Encoded Word:", encoded_word)
    elif user_input == 'd':
        word = input("Enter word to decode: ")
        decoded_word = decode(word)
        print("Decoded Word:", decoded_word)
    else:
        print("Invalid input. Please enter 'e' or 'd'.")

if __name__ == "_main_":
    main()