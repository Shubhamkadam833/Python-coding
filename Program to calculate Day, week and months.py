#Created a program using maths and f-Strings that tells us how many days, weeks, months 
#we have left if we live until 90 years old.
age = input("What is your current age? ")
Days = 32850 - (int(age) * 365)
Weeks = 4680 - (int(age) * 52)
Months = 1080 - (int(age) * 12)
print(f" You have {Days} Days, {Weeks} Weeks, {Months} Months left")