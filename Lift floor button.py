#input
buttons = input("Press '(' for up & ')' for down")
floor , highest_floor , lowest_floor = 0,0,0

#iterate through input
for button in buttons:
    if button == "(":
        floor += 1
        highest_floor += 1
         
    elif button == ")":
        floor -= 1
        lowest_floor -= 1

print("You are at floor" , str(floor) , "\nHighest floor is" , str(highest_floor) , "\nLowest floor is" , str(lowest_floor))

