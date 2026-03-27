# Basic Lead Collector + Analyzer

leads = []
num = int(input("enter number of leads: "))

# Name Collection
for i in range(num):
    name = input(f"Enter lead no. {i+1} name: ")
    leads.append(name)
    
print("\n=== LEADS ENTERED ===")


# ANYLISE
for lead in leads:
    hours = int(input(f"Enter How Many Hours {lead} Works: "))

    if hours < 0:
        result = ("Invalid input")

    elif hours >= 8:
        result = ("Need automation")    

    elif 4 < hours < 8:
        result = ("Good, but still need some automation")    

    elif hours == 4:
        result = ("Good, but still need some automation")

    else:
        result = ("Normal Workload")    
    
   
    print(f"{lead} → {result}")




