import random

correct_guess = random.randint(0, 100)
count = 0
while count < 5:
    guess = int(input("Guess a number btw 0 and 100: "))
    if guess < correct_guess:
        print("Too low, try again")
    elif guess > correct_guess:
        print("Too high, try again")
    else:
        print('Awesome, you are correct')
        break

    count += 1
else:
    print("you tried, but u can try again later")
    print("The correct number is", correct_guess)
