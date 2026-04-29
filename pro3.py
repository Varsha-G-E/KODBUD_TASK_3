import re

password = input("Enter your password: ")

# Conditions
length = len(password) >= 8
number = re.search(r"\d", password)
uppercase = re.search(r"[A-Z]", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Check strength
if length and number and uppercase and special:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")
    print("\nPassword must contain:")
    
    if not length:
        print("- Minimum 8 characters")
    if not number:
        print("- At least 1 number")
    if not uppercase:
        print("- At least 1 uppercase letter")
    if not special:
        print("- At least 1 special character")