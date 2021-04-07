# To play the game, the user has to input the lower bound and upper bound of the range 
# The compiler generates a random integer between the range and store it in a variable for future references.
# If the user guesses a number that is greater or less than the randomly selected number, the user has to retry 
# Once the user gets the correct number, the user gets a "Congratulations" output. 

import random 
import math 

#Taking inputs 
lower = int(input("Enter lower bound number: "))
upper = int(input("Enter upper bound number: "))

#Generating random numbers between the lower and upper 
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

#Initializing the number of guesses
count = 0 

#for calculation of minimum number of guesses depends upon range 
while count < math.log(upper - lower + 1, 2):
    count += 1 

    #Taking guessing number as input 
    guess = int(input("Guess a number: "))

    #Condition testing 
    if x == guess: 
        print("Congratulations you did it in", count, " try")

        #Once guessed, the loop will break 
        break 
    elif x > guess: 
        print('You guessed too small! ')
    elif x < guess: 
        print("You guessed too high!")

# If guessing is more than required guesses, show this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")