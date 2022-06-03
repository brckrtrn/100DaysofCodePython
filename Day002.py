print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
people_count = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, o 15? "))
final_pay = "{:.2f}".format(round(((total_bill * (1 + tip_percentage/100)) / people_count), 2))

print(f"Each person should pay: ${final_pay}")