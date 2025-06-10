import random
import string
def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters  # a-zA-Z
    if use_digits:
        characters += string.digits    # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$...

    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Get user inputs
try:
    length = int(input("Enter desired password length (e.g., 12): "))
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    # Generate password
    password = generate_password(length, use_digits, use_symbols)
    if password:
        print("\n🔐 Your generated password is:", password)
except ValueError:
    print("Please enter a valid number for length.")
