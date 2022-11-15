import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("what do you choose? rock, paper, or scissors?\n Type 0 for rock, 1 for paper, 2 for scissors.\n"))
if choice >= 3 or choice < 0:
    print("invalid choice")
    exit()
else:

    game_images = [rock, paper, scissors]
    print(game_images[int(choice)])

    choice = int(choice)
    computer = random.randint(0,2)
    print("computer chooses",game_images[int(computer)])
    if choice == computer:
        print("It's a tie!")
    elif choice == 0 and computer == 1:
        print(rock)
        print("You lose. Paper covers rock.")
    elif choice == 1 and computer == 2:
        print(paper)
        print("You lose. Scissors cut paper.")
    elif choice == 2 and computer == 0:
        print(scissors)
        print("You lose. Rock smashes scissors.")
    elif choice == 0 and computer == 2:
        print(rock)
        print("You win. Rock crushes scissors.")
    elif choice == 1 and computer == 0:
        print(paper)
        print("You win. Paper covers rock.")
    elif choice == 2 and computer == 1:
        print(scissors)
        print("You win. Scissors cut paper.")
    