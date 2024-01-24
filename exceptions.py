
#Example
try:
    age1 = int(input("What is your age player 1?"))
    age2 = int(input("What is your age player 2?"))
    res= age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")

except ZeroDivisionError:
    print(" I am sorry, but you cannot divide by zero")
except:
    print("I am sorry, but something went wrong")
else:
    print("Player 1 is older tha player 2 by a factor of", res)
finally:
    print("Thank you for playing!")


#Same process as before
age = int(input("What is your age?"))
print(f"Your age is {age}")
print("Your age is", age)


#Catching the exception and assigning a message
try:
    age = int(input("What is your age?"))
except ValueError:
    print(" I am sorry, but that is not a valid number")
else:
    print("Your age is", age)

#Example 2 players, catching errors with more than one value
try:
    age1 = int(input("What is your age player 1?"))
    age2 = int(input("What is your age player 2?"))
    res= age1/age2
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    print("Player 1 is older tha player 2 by a factor of", res)