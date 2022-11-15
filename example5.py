print('''                       ___
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\
         /' %%@=%o%%%o|   /(_)o%%% `\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
question1 = input("you're at a crossroad. Do you want to go left or right? Type 'left' or 'right'\n").lower()
if question1  == "left":
    question2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across the lake.").lower()
    if question2 == "wait":
        question3 = input("you arrive at the island. There, there is a house with 3 doors. One red, one blue, and one yellow. Which one do you choose? \n").lower()
        if question3 == "yellow":
            print("You win!")
            print("")
        else:
            print("Game over.")
    else: 
        print("You drowned.")        
elif question1 == "right":
    print("You fell into a hole. Game over.")
