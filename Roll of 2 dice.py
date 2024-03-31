import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

try:
    #input for number of sides on each die
    sides_die1 = int(input("Enter the number of sides for the first die: "))
    sides_die2 = int(input("Enter the number of sides for the second die: "))

    #check for physically possible dice
    if sides_die1 < 2 or sides_die2 < 2:
        print("Number of sides must be 2 or greater.")
    
    roll1 = roll_dice(sides_die1)
    roll2 = roll_dice(sides_die2)

    print("First die roll: ",roll1)
    print("Second die roll: " ,roll2)
    print("Sum of rolls: ", roll1 + roll2)
except ValueError:
    print("Please enter a valid number of sides (2 or greater).")
#simulate dice rolls
    


