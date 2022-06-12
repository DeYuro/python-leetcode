import random

guess = random.randrange(1,100)
user_input = None
print("Guess number between 1-100")
count = 0
while user_input != guess:
    user_input = int(input())
    if user_input < guess:
        print("Lower, try again")
    elif user_input > guess:
        print("Higher try again")
    count += 1

print(f'Correct with {count} tries')
