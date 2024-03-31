try:
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in m): "))
    
    if weight <= 0 or height <= 0:
        print("Please enter positive values for weight and height.")
        exit()

except ValueError:
    print("Please enter valid numeric values for weight and height.")
    exit()

BMI = float(weight / (height ** 2))

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal weight (Ideal)")
elif 25 <= BMI <= 29.9:
    print("Overweight")
elif BMI >= 30:
    print("Obese")

print("BMI:", round(BMI, 1))

    
