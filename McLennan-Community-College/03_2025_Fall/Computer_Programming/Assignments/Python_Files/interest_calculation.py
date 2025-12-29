investment_amount = int(input("Enter the investment amount: "))
while investment_amount <= 0 or investment_amount >= 50000:
        print("Invalid amount. Please enter a value greater than 0 and less than 50,000.")
        investment_amount = int(input("Enter the investment amount: "))
interest_rate = float(input("Enter the interest rate: "))
while interest_rate <= 0 or interest_rate >= 15:
        print("Invalid rate. Please enter a value greater than 0 and less than 15.")
        interest_rate = float(input("Enter the interest rate: "))
investment_years = int(input("Enter the investment duration in years: "))
while investment_years <= 0:
        print("Invalid duration. Please enter a value greater than 0.")
        investment_years = int(input("Enter the investment duration in years: "))
months = investment_years * 12
monthly_rate = interest_rate / 12 / 100
total = 0

for month in range(1, months + 1):
    total += investment_amount
    interest = round(total * monthly_rate, 2)
    total += interest
    if month % 12 == 0:
        print(f"Year {month // 12}: ${round(total, 2)}")

print(f"\nAfter {investment_years} years at {interest_rate}% yearly interest,")
print(f"with a monthly investment of ${investment_amount},")
print(f"the total investment value after compounding is ${round(total, 2)}")
print("Written by Javier Silva")