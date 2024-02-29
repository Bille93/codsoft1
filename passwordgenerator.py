import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))

    if length < 8:
        print("Please choose a length of at least 8 characters for a strong password.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
