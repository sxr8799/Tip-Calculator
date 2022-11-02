print("Welcome to the tip calculator!")

total_bill = int(input("What was the total bill? "))
tip_percentage = int(input("Please enter your tip percentage without the (%): ")) / 100
number_of_people = int(input("How many people to split the bill? "))
tip_calc = (total_bill / number_of_people) * tip_percentage
bill_total_with_tip = tip_calc + (total_bill/number_of_people)
limited_float = "{:.2f}".format(bill_total_with_tip)
print(f"Each Person should pay: {limited_float}")
