try:
    amnt = float(input("Enter amount of check: $"))
    people = int(input("Enter no of people:"))
    tip = float(input("Enter desired tip as decimal:"))
    total_amnt = amnt * (1 + tip)  
    payer_owes = total_amnt / people
    print("Each payer owes $", round(payer_owes, 2))

except ValueError:
    print("Please enter valid numeric values.")
except ZeroDivisionError:
    print("Number of people cannot be zero.")

