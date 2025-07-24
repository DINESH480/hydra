import re

def check_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[a-z]", password):
        return "Weak: Missing lowercase"
    if not re.search("[A-Z]", password):
        return "Weak: Missing uppercase"
    if not re.search("[0-9]", password):
        return "Weak: Missing digit"
    if not re.search("[!@#$%^&*()_+]", password):
        return "Weak: Missing special character"
    return "Strong Password!"

password = input("Enter your password: ")
print(check_strength(password))
