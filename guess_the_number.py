import random
number = random.randint(1, 100)
a = -1
guesses = 0
while(a!= number):
    guesses += 1
    a = int(input("Guess the number:"))
    if(a> number):
        print("Lower number please!")
    else:
        print("Higher number please!")
print(f"You have guessed the number correctly in {guesses} attempt")    