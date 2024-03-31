fopen = open("data1.txt")

# Mapping of textual representations to numeric values
num_text = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

for line in fopen:
    line = line.strip()
    first_digit = None
    second_digit = None

    for char in line:
        if char.isdigit() and first_digit is None:
            first_digit = char
        elif char.isalpha() and first_digit is None:
            if char.lower() in num_text:
                first_digit = num_text[char.lower()]
        
        if char.isdigit() or char.isalpha():
            if char.isdigit():
                second_digit = char
            elif char.lower() in num_text:
                second_digit = num_text[char.lower()]

    if first_digit is not None and second_digit is not None:
        print(first_digit + second_digit)

fopen.close()
