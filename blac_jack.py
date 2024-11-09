import random

def compare(u_calculate: object, c_calculate):
    if u_calculate == c_calculate:
        return print("equals")
    elif u_calculate == 0:
        return print("win with black jack")
    elif c_calculate == 0:
        return print("lose with black jack")
    elif u_calculate > 21:
        return print("lose with black jack")
    elif c_calculate > 21:
        return print("win with black jack")
    elif u_calculate > c_calculate:
        return print("win with black jack")
    else:
        return print("lose with black jack")



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def display_ascii_art():
    print(r"""
      ____  _            _            _        
     |  _ \| |          | |          | |       
     | |_) | | ___ _ __| |_ ___  ___| | _____  
     |  _ <| |/ _ \ '__| __/ _ \/ __| |/ / _ \ 
     | |_) | |  __/ |  | ||  __/ (__|   <  __/ 
     |____/|_|\___|_|   \__\___|\___|_|\_\___| 

    """)

display_ascii_art()
user_cards = []
user_calcullate = 0
computer_calcullate = 0
computer_cards = []
game_over = True
for i in range(2):
    new_card1 = deal_card()
    new_card2 = deal_card()
    user_cards.append(new_card1)
    computer_cards.append(new_card2)
    print(user_cards[i], computer_cards[i])
while game_over:
    user_calcullate = calculate(user_cards)
    computer_calcullate = calculate(computer_cards)
    print(user_calcullate, computer_calcullate)
    if user_calcullate == 0 and computer_calcullate == 0 and user_calcullate > 21:
        game_over = False
    else:
        user_should_deal = input("do you want card again:")
        if user_should_deal == 'y':
            user_calcullate=user_cards.append(deal_card())
            print(user_calcullate)
            user_calcullate = calculate(user_cards)
        else:
            game_over = False
while not computer_calcullate == 0 or computer_calcullate <= 17:
    computer_should_deal = input("computer  want card again:")
    if computer_should_deal == 'y':
        computer_cards.append(deal_card())
        computer_calcullate = calculate(computer_cards)
        print(user_calcullate, computer_calcullate)

    compare(user_calcullate, computer_calcullate)



