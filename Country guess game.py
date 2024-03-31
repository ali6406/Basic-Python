import random

countries = [
    "United States", "China", "India", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico",
    "Japan", "Philippines", "Vietnam", "Ethiopia", "Egypt", "DR Congo", "Iran", "Turkey", "Germany", "France",
    "United Kingdom", "Italy", "South Africa", "Myanmar", "Tanzania", "South Korea", "Colombia", "Kenya", "Spain",
    "Argentina", "Ukraine", "Uganda", "Algeria", "Sudan", "Iraq", "Poland", "Canada", "Morocco", "Afghanistan",
    "Saudi Arabia", "Peru", "Uzbekistan", "Angola", "Malaysia", "Mozambique", "Ghana", "Yemen", "Nepal",
    "Venezuela", "Madagascar", "Cameroon", "Côte d'Ivoire", "North Korea", "Australia", "Niger", "Taiwan",
    "Sri Lanka", "Burkina Faso", "Mali", "Romania", "Chile", "Kazakhstan", "Zambia", "Guatemala", "Ecuador",
    "Syria", "Netherlands", "Senegal", "Cambodia", "Chad", "Somalia", "Zimbabwe", "Guinea", "Rwanda", "Benin",
    "Burundi", "Tunisia", "Bolivia", "Belgium", "Haiti", "Cuba", "South Sudan", "Dominican Republic", "Czech Republic",
    "Greece", "Jordan", "Portugal", "Azerbaijan", "Sweden", "Honduras", "United Arab Emirates", "Hungary", "Belarus",
    "Tajikistan", "Austria", "Serbia", "Switzerland", "Togo", "Sierra Leone", "Hong Kong"]

Rand_country = random.choice(countries)
rand_country = random.choice(countries).lower()
guesses = "_" * len(rand_country)

while "_" in guesses:
    guess = input("Guess a letter: ").lower()
    new_guess = list(guesses)
    if guess in rand_country:
        for i in range(len(rand_country)):
            if guess == rand_country[i] and new_guess[i] == "_":
                new_guess[i] = guess
        guesses = ''.join(new_guess)
        print("Correct guess:", guesses)
    else:
        print("Wrong guess.")
print("Congrats! You guessed it right! The country is:", rand_country)