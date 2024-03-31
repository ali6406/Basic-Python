try:
    seconds = int(input("Enter the number of seconds: "))
    if seconds < 0:
        print("Please enter a non-negative integer.")
    else:    
        #unit conversions
        days = seconds // (24 * 3600)
        hours = seconds // 3600
        minutes = seconds // 60

        print(days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")
        
except ValueError:
    print("Please enter an integer.")

