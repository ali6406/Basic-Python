import random
no_of_times = int(input("Enter no of times shoes chosen randomly from Shock's collection: ")) 
options = ["White shoe"] * no_of_times + ["Black shoe"] * no_of_times
no_of_mismatch , at_least_one_black = 0 , 0

for i in range(no_of_times):
    shoe1 = random.choice(options)
    shoe2 = random.choice(options)
    if "Black shoe" in [shoe1, shoe2]:
        at_least_one_black += 1
        if shoe1 != shoe2: 
            no_of_mismatch += 1
probability_with_one_black = round(no_of_mismatch / at_least_one_black , 4)
print("Probability of mismatch with at least one black shoe is seen: ", probability_with_one_black)
print("Probability of matching with at least one black shoe is seen: ", round(1 - probability_with_one_black , 4))
