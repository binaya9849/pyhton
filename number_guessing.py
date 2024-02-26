import random
import math

lower = int(input("Enter lower bound:"))
upper = int(input("Enter uper bound:"))


x = random.randint(lower , upper)
print("\n\tYou've only",
      round(math.log(upper - lower + 1 , 2)),
      "chances to guess the interger!/n")

count = 0

while count < math.log(upper - lower +1 , 2):
    count += 1
    guess = int(input("Guess a umber:"))

    if x == guess:
        print("hats up brother", count , "try")

        break
    elif x > guess:
        print("too small bro")
    elif x < guess:
        print("too big bro ")

if count >= math.log(upper-lower+1,2):
    print("\n the number is " % x)
    print("\tBetter luck next time")
    