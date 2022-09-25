import random
art = """
      _        _          __            _           ______                             
     / \      (_)        [  |          | |        .' ___  |                            
    / _ \     __   .---.  | |--.   ,--.\_|.--.   / .'   \_|  ,--.   _ .--..--.  .---.  
   / ___ \   [  | / /'`\] | .-. | `'_\ : ( (`\]  | |   ____ `'_\ : [ `.-. .-. |/ /__\\ 
 _/ /   \ \_  | | | \__.  | | | | // | |, `'.'.  \ `.___]  |// | |, | | | | | || \__., 
|____| |____|[___]'.___.'[___]|__]\'-;__/[\__) )  `._____.' \'-;__/[___||__||__]'.__.' 
                                                                                       
"""

guess = 0
answer = random.randint(1, 100)
print(art)
print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
level = input("choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    attempts = 5
print("you have", attempts,"attempts remaining to guess the number.")
guess = int(input("make a guess: "))
while guess != answer:
    if guess > answer:
        print("too high")
        attempts -= 1
        print("you have", attempts,"attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
    elif guess < answer:
        print("too low")
        attempts -= 1
        print("you have", attempts,"attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
    else:
        print("you got it! The answer was", answer)
        break
    if attempts == 0:
        print("you've run out of guesses, you lose.")
        break

