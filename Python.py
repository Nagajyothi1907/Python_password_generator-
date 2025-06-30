import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    has_number = False
    has_special = False

    while len(password) < min_length or (numbers and not has_number) or (special_characters and not has_special):
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

    return password

# User input
min_length = int(input("Enter the minimum length: ")) 
has_number = input("Do you want to have numbers (yes/no)? ").strip().lower() == "yes"
has_special = input("Do you want to have special characters (yes/no)? ").strip().lower() == "yes"


pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
