print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to tip? "))
people = int(input("How many people should we split the bill between? "))

total_tip = tip / 100 * bill
total_bill = total_tip + bill
bill_each = round(total_bill / people, 2)
print(f"Each person should pay ${bill_each}.")
