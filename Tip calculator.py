#Welcome to the tip calculator
print("Welcome to the tip calculator")
Bill = int(input("what was the total Bill?"))
print(f"The bill is {Bill} Dollars")
Tips = input("what percentage you would like to give 10, 12 or 15 ?")
Tips1 = int(Tips)
print(f"the tip you have given is {Tips1} %")
Total_Bill = (Bill * Tips1/ 100 ) + Bill
print(f"Therefore total bill is {Total_Bill} dollars")
split_share = int(input("how many people to split the bill? "))
split_shares = Total_Bill / split_share
print(f"Each person should pay {split_shares} dollars")
