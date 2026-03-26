# Favorite Items List

items = []

n = int(input("How many items do you want to add: "))

# taking input
for i in range(n):
    item = input(f"Enter item {i+1}: ")
    items.append(item)

# output
print("\n=== Your Items ===")

for item in items:
    print(item)
