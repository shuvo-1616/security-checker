import random
import string
import re
def check_strength(pw):
    if len(pw) < 6:
        return "Weak (Too short)"
    s = 0
    if any(c.islower() for c in pw): s += 1
    if any(c.isupper() for c in pw): s += 1
    if any(c.isdigit() for c in pw): s += 1
    if any(c in string.punctuation for c in pw): s += 1
    return ["Weak", "Medium", "Strong"][s-2] if s >= 2 else "Weak"
def generate_pw(n=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11 and phone.startswith('01')
def is_valid_username(username):
    return username.isalnum() and len(username) >= 4
while True:
    print("\n Security System Menu:")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Check Email Validity")
    print("4. Check Phone Number")
    print("5. Check Username")
    print("6. Exit")
    op = input("Choose an option: ")
    if op == '1':
        pw = input(" Enter your password: ")
        print("✅ Strength:", check_strength(pw))
    elif op == '2':
        print("Generated Pasword:", generate_pw())
    elif op == '3':
        email = input(" Enter email: ")
        print("✅ Valid" if is_valid_email(email) else "❌ Invalid email format")
    elif op == '4':
        phone = input("Enter phone number: ")
        print("✅ Valid" if is_valid_phone(phone) else "❌ Invalid phone number")
    elif op == '5':
        username = input(" Enter username: ")
        print("✅ Valid" if is_valid_username(username) else "❌ Username must be 4+ characters and alphanumeric")
    elif op == '6':
        print("Exiting... Stau Safe!")
        break
    else:
        print("❌ Invalid choice. Try again.")
