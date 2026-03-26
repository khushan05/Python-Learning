# Login System

print("=== Secure Login System ===")

correct_password = "fitdude123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted ✅")
        break
    else:
        attempts += 1
        print(f"Wrong Password ❌ | Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Account Locked 🔒")