import re
import random
import string
import pyautogui
import time

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak: Include at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Weak: Include at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Include at least one special character."
    
    return "Strong"

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

# Function to save password in Notepad
def save_to_notepad(password):
    pyautogui.hotkey('win', 'r')  # Open Run dialog
    time.sleep(1)
    pyautogui.typewrite("notepad\n", interval=0.1)
    time.sleep(2)
    pyautogui.typewrite(f"Your Strong Password: {password}\n", interval=0.1)

# Get user input
user_password = input("Enter a password: ")

# Check password strength
strength = check_password_strength(user_password)
print("Password Strength:", strength)

if "Weak" in strength:
    new_password = generate_strong_password()
    print("Generated Strong Password:", new_password)
    
    # Save strong password to Notepad
    save_to_notepad(new_password)
else:
    print("Your password is strong!")
