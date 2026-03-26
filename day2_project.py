# Smart Decision System

print("=== Life Category Checker ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n=== Result ===")

if age < 13:
    print(f"{name}, you are a Child 👶")
    print("Focus on learning and having fun!")

elif 13 < age < 20:
    print(f"{name}, you are a Teenager 🔥")
    print("Start building skills and discipline.")

elif 20 < age < 30:
    print(f"{name}, you are a Young Adult 🚀")
    print("This is your grinding phase. Build your future.")

else:
    print(f"{name}, you are an Adult 💼")
    print("Focus on stability and smart decisions.")