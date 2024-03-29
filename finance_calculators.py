import math

calculation = input('''
    investment - to calculate the amount of interest you will earn on your investment
    bond       - to calculate the amount you will have to pay on a home loan
                    
    Enter either 'investment' or 'bond' from the menu above to proceed:
    '''
    )

modified_calculation = calculation.lower()  # Modifying every manipulation of investment/bond to one

if modified_calculation == "investment":
    amount = int(input("Enter amount of money that you are depositing: "))
    rate = int(input("Enter interest rate percentage (do not add %): "))
    time = int(input("Enter the number of investment years: "))
    interest = input("Select your interest (simple/compound): ")

    if interest == "simple":
        total = round(amount * (1 + (rate/100) * time), 2)  # Money takes 2 decimal places
        print(f"Investment interest amount: {total}")
    elif interest == "compound":
        total = round(amount * math.pow((1 + (rate/100)), time), 2)
        print(f"Investment interest amount: {total}")
    else:
        print("Error: Invalid interest type")

elif modified_calculation == "bond":
    value = int(input("Enter home present value: "))
    rate = int(input("Enter interest rate percentage (do not add %): "))
    time = int(input("Enter number of repayment months: "))
    
    interest_rate = (rate/100) / 12  # Storing divided rate into variable to prevent too much dividing in formula

    total = round((interest_rate * value) / (1 - (1 + interest_rate)**(-time)), 2)
    print(f"Home loan repayment amount: {total}")

else:
    print("Error: Invalid calculation")