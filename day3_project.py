# Number Analyzer

print("=== Number Analyzer ===")

num = int(input("Enter a number: "))

print("\n=== Result ===")

# Even / Odd
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# Divisible by 3
if num % 3 == 0:
    print("Divisible by 3")

# Divisible by 5
if num % 5 == 0:
    print("Divisible by 5")

# Special case
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5 🔥")