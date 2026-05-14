# =================================================
# SECURE AUTHENTICATION SYSTEM
# Cybersecurity Project 
# =================================================

import hashlib

# ================= DATABASES =================

users = {}
login_history = []

# ================= HEADER =================

print("\n=================================================")
print("      SECURE AUTHENTICATION SYSTEM 🔐")
print("=================================================\n")

print("Authentication system with password security checks")
print("and login tracking for cybersecurity awareness.\n")


# ================= PASSWORD HASHING =================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ================= REGISTER =================

def register():

    print("\n========== USER REGISTRATION ==========")

    while True:

        username = input("Create username: ").strip()

        if username in users:
            print("⚠ Username already exists. Try again.")
            continue

        if len(username) < 3:
            print("⚠ Username must be at least 3 characters.")
            continue

        break

    while True:

        password = input("Create password: ")
        confirm_password = input("Confirm password: ")

        if password != confirm_password:
            print("⚠ Passwords do not match. Try again.")
            continue

        errors = []

        if len(password) < 6:
            errors.append("Minimum 6 characters")

        if not any(c.isupper() for c in password):
            errors.append("At least one uppercase letter")

        if not any(c.isdigit() for c in password):
            errors.append("At least one number")

        if not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for c in password):
            errors.append("At least one special character")

        if errors:
            print("\n⚠ Password does not meet requirements:")
            for e in errors:
                print("-", e)
            print("\nTry again ONLY password.\n")
        else:
            break

    users[username] = hash_password(password)

    print("\n✅ Registration successful!")
    login_history.append(f"{username} registered successfully")


# ================= LOGIN =================

def login():

    print("\n========== LOGIN ==========")

    username = input("Username: ").strip()

    if username not in users:
        print("❌ User not found.")
        return

    while True:

        password = input("Password: ")

        if users[username] == hash_password(password):

            print("\n✅ Login successful!")
            print("👋 Welcome back!\n")

            login_history.append(f"{username} logged in successfully")
            break

        else:
            print("❌ Incorrect password. Try again only password.\n")
            login_history.append(f"{username} failed login attempt")


# ================= HISTORY =================

def show_history():

    print("\n========== LOGIN HISTORY ==========")

    if len(login_history) == 0:
        print("No login activity yet.\n")
        return

    for item in login_history:
        print("-", item)

    print()


# ================= MENU =================

def show_menu():

    print("\n========== MAIN MENU ==========")
    print("1. Register")
    print("2. Login")
    print("3. View Login History")
    print("4. Exit")
    print("================================")


# ================= MAIN LOOP =================

while True:

    show_menu()
    choice = input("Choose option (1-4): ").strip()

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        show_history()

    elif choice == "4":
        print("\n================================")
        print("🙏 Thank you for using the system")
        print("🔐 Stay safe in the digital world")
        print("================================\n")
        break

    else:
        print("⚠ Invalid option. Try again.")
