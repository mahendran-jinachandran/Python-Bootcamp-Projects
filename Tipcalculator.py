print("Welcome to the tip calculator")
total_bill = float(input("How much was the bill?"))

tip_alloted = float(input("How much tip would you like to give? 10%, 12% or 15%"))
tip_amount = (tip_alloted / 100) * total_bill

total_amount = total_bill + tip_amount
number_person = int(input("How many people to split the bill?"))

print(f"Total Bill: {total_amount / number_person}")
