from art import logo
import random
computer_cards = []
player_cards = []
my_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False
def deal_cards():
    """This function deals two cards to the player and the computer"""
    for card in range(2):   #card is a variable that is used to iterate through the range of 2
        player_cards.append(random.choice(my_deck))
        computer_cards.append(random.choice(my_deck))
def calculate_score(cards):
    """This function calculates the score of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        #blackjack, wins
        return 0
    if 11 in cards and sum(cards) > 21:
        #if there is an ace and the sum is greater than 21, the ace is 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """This function compares the scores and determines the winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(logo)
    #Deal the user and computer 2 cards each using deal_cards()
    deal_cards()
    game_over = False
    computer_cards.append(deal_cards())
    player_cards.append(deal_cards())
    while not game_over:
        user_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(random.choice(my_deck))
            else:
                game_over = True


    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        again = input("Type 'y' to get another card, type 'n' to pass: ")
        if again == "y":
            player_cards.append(random.choice(my_deck))
        else:
            game_over = True
    