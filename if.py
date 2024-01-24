import random

try:
    age= int(input("How old are you? "))
    country = input("Where do you live? ")
    drinks = ["beer","wine","vodka"]
except ValueError:
    print("I am sorry but that is not a valid number ")
else:
    #do some sanity checks on age
    if age < 0 or age > 130:
        print("i am sorry but age cant be negative or greater than 130")

    elif age < 18:
        print("Youre too young for this game go away")

    elif age < 21 and country == "US":
        print("Sorry, you cant drink")
    else:
        drink = random.choice(drinks)
        print("Take a shot of", drink," thank you for playing, you are", age, "years old!")

