# Life Profile Builder

print("=== Welcome to Life Profile Builder ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
goal = input("What is your life goal: ")
hobby = input("What is your hobby: ")
birthday_passed = input("Have you had your birthday this year? (yes/no): ")

# calculation
current_year = 2026
birth_year = current_year - age

if birthday_passed == "yes":
    birth_year = 2026 - age
else:
    birth_year = 2026 - age - 1

    
# output
print("\n=== Your Profile ===")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Goal: {goal}")
print(f"Estimated Birth Year: {birth_year}")

print("\n=== Summary ===")
print(f"Hey, I'm {name} from {city}.")
print(f"I'm {age} years old and I enjoy {hobby}.")
print(f"My goal is to become {goal}.")
print(f"I was born around {birth_year}.")