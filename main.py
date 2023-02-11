cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from art import logo


def deal_card(player, number):
    zero = 0
    while zero < number:
        x = random.choice(cards)
        player.append(x)
        zero += 1
    return player


def calculate_score(player):
    score = 0
    for card in player:
        score += card
    if score > 21 and cards[0] in player:
        score -= 10
        if score > 21:
            print("Bust!")
    elif score > 21 and cards[0] not in player:
        print("Bust!")
    return score


def compare(player, computer):
    x = sum(player)
    y = sum(computer)
    outcome = ""
    if y >= 17:
        if x > y and x <= 21:
            outcome = "Player wins"
        if y > x and y <= 21:
            outcome = "Computer wins"
        if x == y and x > 17:
            outcome = "Draw"
    if x > 21:
        outcome = "Computer wins"
    if y > 21:
        outcome = "Player wins"
    return outcome


keep_playing = True
while keep_playing == True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if play == 'y':
        print(logo)
        user_cards = []
        computer_cards = []
        deal_card(user_cards, 2)
        deal_card(computer_cards, 2)
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        first_card = computer_cards[0]
        print(f"Computer's first card: {first_card}")
        game_active = True
        while game_active == True:
            draw_another = input(
                "Type 'y' to get another card, type 'n' to pass:")
            if draw_another == 'y':
                deal_card(user_cards, 1)
                print(user_cards)
                user_score = calculate_score(user_cards)
                print(user_score)
                if user_score > 21:
                    print(compare(user_cards, computer_cards))
                    game_active == False
                    break
            if draw_another == 'n':
                computer_score = calculate_score(computer_cards)
                while computer_score < 17:
                    deal_card(computer_cards, 1)
                    print(computer_cards)
                    computer_score = calculate_score(computer_cards)
                    print(computer_score)
                game_active = False
                print(compare(user_cards, computer_cards))
else:
    print("Bye")
    keep_playing = False
