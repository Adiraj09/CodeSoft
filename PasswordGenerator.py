import random
import string

def generate_password(length):
    if length < 1:
        return "Password length should be at least 1"
    
    # Define character sets for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_chars = lower + upper + digits + special
    
    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(all_chars)
    for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter an integer value for the length.")
        return
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
